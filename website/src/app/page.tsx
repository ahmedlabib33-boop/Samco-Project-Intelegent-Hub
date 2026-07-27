import Link from "next/link";
import portfolio from "../../public/data/portfolio.json";

type ProjectRecord = {
  project_id: string;
  project_key: string;
  project_folder_name: string;
  project_display_name: string;
  sector: string;
  status: string;
  contract_value: number | null;
  paid_amount: number | null;
  spent_amount: number | null;
  remaining_value: number | null;
  planned_progress: number | null;
  actual_progress: number | null;
  progress_variance: number | null;
  spi: number | null;
  cpi: number | null;
  risk_score: number | null;
  delay_days: number | null;
  claims_exposure: number | null;
  data_quality: number | null;
  decision_required: boolean;
};

type SectorRecord = {
  sector: string;
  project_count: number;
  contract_value: number;
  paid_amount: number;
  spent_amount: number;
  average_progress: number | null;
  average_spi: number | null;
  average_cpi: number | null;
  average_risk_score: number | null;
  delayed_projects: number;
  decisions_required: number;
};

const projects = portfolio.projects as ProjectRecord[];
const sectors = portfolio.sectors as SectorRecord[];
const totals = portfolio.totals;

function numberValue(value: number | null | undefined, digits = 0) {
  if (value === null || value === undefined || Number.isNaN(value) || !Number.isFinite(value)) return "N/A";
  return new Intl.NumberFormat("en-US", { maximumFractionDigits: digits, minimumFractionDigits: digits }).format(value);
}

function money(value: number | null | undefined) {
  if (value === null || value === undefined || Number.isNaN(value) || !Number.isFinite(value)) return "N/A";
  return `EGP ${new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 }).format(value)}`;
}

function percent(value: number | null | undefined) {
  if (value === null || value === undefined || Number.isNaN(value) || !Number.isFinite(value)) return "N/A";
  return `${(value * 100).toFixed(1)}%`;
}

function statusClass(value: number | null | undefined, target = 1) {
  if (value === null || value === undefined || !Number.isFinite(value)) return "neutral";
  if (value >= target) return "good";
  if (value >= target * 0.9) return "watch";
  return "critical";
}

function KpiCard({
  label,
  value,
  note,
  status
}: {
  label: string;
  value: string;
  note: string;
  status: "good" | "watch" | "critical" | "neutral";
}) {
  return (
    <article className="kpi-card">
      <div className="kpi-top">
        <span>{label}</span>
        <b className={`badge ${status}`}>{status}</b>
      </div>
      <strong>{value}</strong>
      <small>{note}</small>
    </article>
  );
}

function BarChart({ rows, field }: { rows: ProjectRecord[]; field: keyof ProjectRecord }) {
  const max = Math.max(...rows.map((row) => Number(row[field] || 0)), 1);
  return (
    <div className="bars">
      {rows.map((row) => {
        const value = Number(row[field] || 0);
        return (
          <div className="bar-row" key={`${row.project_key}-${String(field)}`}>
            <span>{row.project_display_name}</span>
            <div><i style={{ width: `${Math.max(4, (value / max) * 100)}%` }} /></div>
            <b>{field.toString().includes("progress") ? percent(value) : money(value)}</b>
          </div>
        );
      })}
    </div>
  );
}

function DonutChart() {
  const total = Math.max(sectors.reduce((sum, sector) => sum + sector.project_count, 0), 1);
  let offset = 0;
  const colors = ["#38d7d2", "#d6a23a", "#63a8ff", "#a78bfa", "#4ade80"];
  return (
    <div className="donut-wrap">
      <svg viewBox="0 0 42 42" className="donut">
        <circle cx="21" cy="21" r="15.915" fill="transparent" stroke="#183b5a" strokeWidth="6" />
        {sectors.map((sector, index) => {
          const value = (sector.project_count / total) * 100;
          const dash = `${value} ${100 - value}`;
          const currentOffset = offset;
          offset -= value;
          return (
            <circle
              key={sector.sector}
              cx="21"
              cy="21"
              r="15.915"
              fill="transparent"
              stroke={colors[index % colors.length]}
              strokeWidth="6"
              strokeDasharray={dash}
              strokeDashoffset={currentOffset}
            />
          );
        })}
      </svg>
      <div className="legend">
        {sectors.map((sector, index) => (
          <span key={sector.sector}><i style={{ background: colors[index % colors.length] }} />{sector.sector}: {sector.project_count}</span>
        ))}
      </div>
    </div>
  );
}

function Scatter() {
  return (
    <svg viewBox="0 0 720 330" className="chart-svg">
      <rect x="40" y="25" width="650" height="260" rx="14" />
      <line x1="70" y1="250" x2="660" y2="250" />
      <line x1="70" y1="250" x2="70" y2="55" />
      <text x="70" y="302">SPI / progress position</text>
      {projects.map((project, index) => {
        const progress = Math.max(0, Math.min(1, project.actual_progress ?? 0));
        const risk = Math.max(0, Math.min(100, project.risk_score ?? 40));
        const x = 80 + progress * 560;
        const y = 245 - (Math.min(project.spi ?? 0.8, 1.2) / 1.2) * 180;
        const size = 10 + risk / 10;
        return (
          <g key={project.project_key}>
            <circle cx={x} cy={y} r={size} className={`bubble ${project.decision_required ? "critical-fill" : "good-fill"}`} opacity="0.9" />
            <text x={x + 14} y={y + 4}>{project.project_display_name}</text>
          </g>
        );
      })}
    </svg>
  );
}

export default function HomePage() {
  return (
    <main>
      <section className="hero">
        <div>
          <p className="eyebrow">Decision Making Dashboard</p>
          <h1>Project Intelligence Hub</h1>
          <p>Executive portfolio website generated from isolated project folders and synced through GitHub for Vercel deployment.</p>
        </div>
        <div className="hero-panel">
          <b>{portfolio.project_count}</b>
          <span>recognized projects</span>
          <small>Last generated: {portfolio.generated_at}</small>
        </div>
      </section>

      <section className="kpi-grid">
        <KpiCard label="Total Projects" value={numberValue(portfolio.project_count)} note={`${portfolio.sector_count} sectors`} status="neutral" />
        <KpiCard label="Total Contract Value" value={money(totals.contract_value)} note="Portfolio BAC / contract value" status="neutral" />
        <KpiCard label="Total Paid" value={money(totals.paid_amount)} note="From project payment files" status="neutral" />
        <KpiCard label="Remaining Value" value={money(totals.remaining_value)} note="Contract less paid/spent" status="watch" />
        <KpiCard label="Average Progress" value={percent(totals.average_progress)} note="Weighted where contract value exists" status={statusClass(totals.average_progress, 0.75)} />
        <KpiCard label="Delayed Projects" value={numberValue(totals.delayed_projects)} note="Delay days or SPI below 1.00" status={totals.delayed_projects > 0 ? "critical" : "good"} />
        <KpiCard label="Average SPI" value={numberValue(totals.average_spi, 2)} note="Earned value schedule index" status={statusClass(totals.average_spi)} />
        <KpiCard label="Average CPI" value={numberValue(totals.average_cpi, 2)} note="Earned value cost index" status={statusClass(totals.average_cpi)} />
      </section>

      <section className="tabs">
        <input id="tab-overall" name="dashboard-tab" type="radio" defaultChecked />
        <input id="tab-sector" name="dashboard-tab" type="radio" />
        <input id="tab-projects" name="dashboard-tab" type="radio" />
        <div className="tab-labels">
          <label htmlFor="tab-overall">Overall Portfolio</label>
          <label htmlFor="tab-sector">Sector Analysis</label>
          <label htmlFor="tab-projects">Projects Analysis</label>
        </div>
        <div className="tab-panels">
          <section id="overall" className="tab-panel">
            <div className="section-title"><h2>Overall Portfolio</h2><span>Portfolio-level command view</span></div>
            <div className="dashboard-grid">
              <article className="panel"><h3>Sector Distribution</h3><DonutChart /></article>
              <article className="panel"><h3>Budget Allocation</h3><BarChart rows={projects} field="contract_value" /></article>
              <article className="panel wide"><h3>Progress Overview</h3><Scatter /></article>
            </div>
          </section>
          <section id="sector" className="tab-panel">
            <div className="section-title"><h2>Sector Analysis</h2><span>Grouped by sector folder</span></div>
            <div className="sector-grid">
              {sectors.map((sector) => (
                <article className="panel" key={sector.sector}>
                  <h3>{sector.sector}</h3>
                  <div className="metric-list">
                    <span>Projects <b>{sector.project_count}</b></span>
                    <span>Budget <b>{money(sector.contract_value)}</b></span>
                    <span>Paid <b>{money(sector.paid_amount)}</b></span>
                    <span>Progress <b>{percent(sector.average_progress)}</b></span>
                    <span>SPI <b>{numberValue(sector.average_spi, 2)}</b></span>
                    <span>CPI <b>{numberValue(sector.average_cpi, 2)}</b></span>
                    <span>Decisions <b>{sector.decisions_required}</b></span>
                  </div>
                </article>
              ))}
            </div>
          </section>
          <section id="projects" className="tab-panel">
            <div className="section-title"><h2>Projects Analysis</h2><span>Open any isolated project deep dive</span></div>
            <div className="project-grid">
              {projects.map((project) => (
                <article className="project-card" key={project.project_key}>
                  <div>
                    <b>{project.project_display_name}</b>
                    <span>{project.sector} / {project.status}</span>
                  </div>
                  <div className="metric-list">
                    <span>Contract <b>{money(project.contract_value)}</b></span>
                    <span>Paid <b>{money(project.paid_amount)}</b></span>
                    <span>Progress <b>{percent(project.actual_progress)}</b></span>
                    <span>SPI <b>{numberValue(project.spi, 2)}</b></span>
                    <span>CPI <b>{numberValue(project.cpi, 2)}</b></span>
                    <span>Risk <b>{numberValue(project.risk_score, 1)}</b></span>
                  </div>
                  <Link href={`/project/${project.project_key}`}>Open project website</Link>
                </article>
              ))}
            </div>
          </section>
        </div>
      </section>
    </main>
  );
}
