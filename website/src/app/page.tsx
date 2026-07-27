"use client";

import { useMemo, useState } from "react";
import portfolio from "../../public/data/portfolio.json";

type ReportKey = "executive_dashboard" | "master_dashboard" | "elite_svg_charts" | "linked_executive_dashboard";

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
  activity_count: number;
  milestone_count: number;
  last_updated: string | null;
  source_files: Record<string, number>;
  reports: Record<ReportKey, string>;
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

const reportTabs: Array<{ key: ReportKey; label: string; note: string }> = [
  { key: "executive_dashboard", label: "Executive Dashboard", note: "Portfolio-style project summary" },
  { key: "master_dashboard", label: "Master Dashboard", note: "Detailed section dashboard" },
  { key: "elite_svg_charts", label: "Elite SVG Charts", note: "Digital chart package" },
  { key: "linked_executive_dashboard", label: "Linked Dashboard", note: "Linked executive HTML" }
];

const workspaceTabs = [
  "Overview",
  "EBS / WBS",
  "Activities",
  "Milestones",
  "S-Curve",
  "EVM",
  "Contracts",
  "Risk Matrix",
  "Letters Intelligence",
  "Delay Analysis",
  "Contract & Claims",
  "Output Studio"
] as const;

type WorkspaceTab = (typeof workspaceTabs)[number];

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

function safeRatio(value: number | null | undefined, target = 1) {
  if (value === null || value === undefined || !Number.isFinite(value)) return 0;
  return Math.max(0.03, Math.min(1, value / target));
}

function statusTone(value: number | null | undefined, target = 1) {
  if (value === null || value === undefined || !Number.isFinite(value)) return "neutral";
  if (value >= target) return "good";
  if (value >= target * 0.9) return "watch";
  return "critical";
}

function HoloKpi({
  title,
  value,
  note,
  tone = "neutral"
}: {
  title: string;
  value: string;
  note: string;
  tone?: "cyan" | "gold" | "blue" | "green" | "red" | "violet" | "neutral" | "good" | "watch" | "critical";
}) {
  return (
    <article className={`holo-kpi tone-${tone}`}>
      <div className="holo-kpi__signal" />
      <span>{title}</span>
      <strong>{value}</strong>
      <small>{note}</small>
    </article>
  );
}

function ProjectNetwork({ selectedProject }: { selectedProject: ProjectRecord }) {
  return (
    <svg className="network-map" viewBox="0 0 720 390" role="img" aria-label="Interactive project network">
      <defs>
        <filter id="glow">
          <feGaussianBlur stdDeviation="5" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>
      <path className="network-line dashed" d="M76 300 C174 130 302 292 420 106 C510 8 566 142 640 72" />
      <path className="network-line" d="M95 292 L285 214 L432 120 L636 78" />
      <path className="network-line soft" d="M285 214 L360 318 L636 78" />
      {projects.map((project, index) => {
        const points = [
          { x: 95, y: 292, color: "#39d7d2" },
          { x: 285, y: 214, color: "#d6a23a" },
          { x: 432, y: 120, color: "#63a8ff" },
          { x: 636, y: 78, color: "#a78bfa" }
        ];
        const point = points[index % points.length];
        const active = project.project_key === selectedProject.project_key;
        return (
          <g key={project.project_key} className={active ? "network-node active" : "network-node"}>
            <circle cx={point.x} cy={point.y} r={active ? 43 : 32} fill={point.color} filter="url(#glow)" />
            <text x={point.x + 48} y={point.y + 5}>{project.project_folder_name}</text>
          </g>
        );
      })}
    </svg>
  );
}

function SignalBar({ label, value, tone }: { label: string; value: number | null | undefined; tone: string }) {
  const width = `${Math.round(safeRatio(value, 1) * 100)}%`;
  return (
    <div className="signal-bar">
      <span>{label}</span>
      <div><i className={`tone-${tone}`} style={{ width }} /></div>
      <b>{percent(value)}</b>
    </div>
  );
}

function Gauge({ label, value, tone }: { label: string; value: number | null | undefined; tone: string }) {
  const percentValue = Math.round(safeRatio(value, 1) * 100);
  return (
    <article className={`gauge tone-${tone}`}>
      <svg viewBox="0 0 160 100">
        <path d="M24 78 A56 56 0 0 1 136 78" className="gauge-track" />
        <path
          d="M24 78 A56 56 0 0 1 136 78"
          className="gauge-fill"
          pathLength="100"
          strokeDasharray={`${percentValue} ${100 - percentValue}`}
        />
      </svg>
      <strong>{numberValue(value, 2)}</strong>
      <span>{label}</span>
    </article>
  );
}

function ProjectConsole({ selectedProject }: { selectedProject: ProjectRecord }) {
  return (
    <section className="project-console">
      <div className="console-head">
        <div>
          <p className="eyebrow">Active Project Digital Twin</p>
          <h2>{selectedProject.project_display_name}</h2>
          <span>{selectedProject.sector} / {selectedProject.status} / Last update: {selectedProject.last_updated || "N/A"}</span>
        </div>
        <b className={`decision-pill ${selectedProject.decision_required ? "critical" : "good"}`}>
          {selectedProject.decision_required ? "Decision Required" : "No Immediate Decision"}
        </b>
      </div>
      <div className="console-grid">
        <HoloKpi title="Contract Value" value={money(selectedProject.contract_value)} note="Selected project value" tone="gold" />
        <HoloKpi title="Actual Progress" value={percent(selectedProject.actual_progress)} note={`Planned ${percent(selectedProject.planned_progress)}`} tone="cyan" />
        <HoloKpi title="SPI" value={numberValue(selectedProject.spi, 2)} note="Schedule performance" tone={statusTone(selectedProject.spi) as "good" | "watch" | "critical" | "neutral"} />
        <HoloKpi title="CPI" value={numberValue(selectedProject.cpi, 2)} note="Cost performance" tone={statusTone(selectedProject.cpi) as "good" | "watch" | "critical" | "neutral"} />
        <HoloKpi title="Activities" value={numberValue(selectedProject.activity_count)} note="Activity records loaded" tone="blue" />
        <HoloKpi title="Data Quality" value={`${numberValue(selectedProject.data_quality, 1)}%`} note="Source completeness" tone="violet" />
      </div>
    </section>
  );
}

function SourceRegister({ project }: { project: ProjectRecord }) {
  return (
    <section className="glass-panel source-register">
      <div className="section-header">
        <div>
          <p className="eyebrow">Source Register</p>
          <h2>Selected Project Data Feed</h2>
        </div>
        <span>{Object.values(project.source_files).reduce((sum, count) => sum + count, 0)} rows recognized</span>
      </div>
      <div className="source-grid">
        {Object.entries(project.source_files).map(([name, count]) => (
          <span key={name}>{name}<b>{count}</b></span>
        ))}
      </div>
    </section>
  );
}

function MiniMetric({ label, value, note }: { label: string; value: string; note: string }) {
  return (
    <article className="mini-metric">
      <span>{label}</span>
      <strong>{value}</strong>
      <small>{note}</small>
    </article>
  );
}

function DataStatus({ label, count }: { label: string; count: number | undefined }) {
  const available = Boolean(count && count > 0);
  return (
    <span className={available ? "data-status available" : "data-status missing"}>
      {label}<b>{available ? `${count} rows` : "No data"}</b>
    </span>
  );
}

function WorkspaceTabContent({
  project,
  activeTab,
  selectedReport,
  setSelectedReport
}: {
  project: ProjectRecord;
  activeTab: WorkspaceTab;
  selectedReport: ReportKey;
  setSelectedReport: (key: ReportKey) => void;
}) {
  if (activeTab === "Overview") {
    return (
      <div className="workspace-grid">
        <MiniMetric label="Project" value={project.project_folder_name} note={project.project_display_name} />
        <MiniMetric label="Status" value={project.status} note={`${project.sector} sector`} />
        <MiniMetric label="Contract Value" value={money(project.contract_value)} note="Project source value" />
        <MiniMetric label="Remaining Value" value={money(project.remaining_value)} note="Contract less paid/spent" />
        <MiniMetric label="Planned Progress" value={percent(project.planned_progress)} note="Planned progress source" />
        <MiniMetric label="Actual Progress" value={percent(project.actual_progress)} note="Actual progress source" />
      </div>
    );
  }

  if (activeTab === "EBS / WBS") {
    return (
      <div className="workspace-two">
        <div>
          <h3>EBS / WBS Register</h3>
          <p>Shows the selected project structure and work breakdown availability from its own folder only.</p>
          <DataStatus label="WBS" count={project.source_files.projects ? project.source_files.projects : undefined} />
        </div>
        <iframe src={project.reports.master_dashboard} title={`${project.project_display_name} master dashboard WBS`} />
      </div>
    );
  }

  if (activeTab === "Activities") {
    return (
      <div className="workspace-grid">
        <MiniMetric label="Activities Loaded" value={numberValue(project.activity_count)} note="Activity source records" />
        <MiniMetric label="Progress Records" value={numberValue(project.source_files.progress)} note="Progress update rows" />
        <MiniMetric label="EVM Records" value={numberValue(project.source_files.evm)} note="Earned value rows" />
        <MiniMetric label="Delay Events" value={numberValue(project.source_files.delay_events)} note="Delay event records" />
      </div>
    );
  }

  if (activeTab === "Milestones") {
    return (
      <div className="workspace-grid">
        <MiniMetric label="Milestones" value={numberValue(project.milestone_count)} note="Milestone records loaded" />
        <MiniMetric label="Schedule Health" value={numberValue(project.spi, 2)} note="SPI schedule indicator" />
        <MiniMetric label="Delayed Days" value={numberValue(project.delay_days)} note="Delay days from project data" />
      </div>
    );
  }

  if (activeTab === "S-Curve") {
    return (
      <div className="workspace-two">
        <div>
          <h3>S-Curve</h3>
          <p>Uses the selected project progress and generated dashboard outputs. If the source S-curve file is missing, the report remains available with controlled source notes.</p>
          <DataStatus label="Progress Updates" count={project.source_files.progress} />
        </div>
        <iframe src={project.reports.linked_executive_dashboard} title={`${project.project_display_name} linked dashboard`} />
      </div>
    );
  }

  if (activeTab === "EVM") {
    return (
      <div className="workspace-grid">
        <MiniMetric label="BAC" value={money(project.contract_value)} note="Budget at completion" />
        <MiniMetric label="PV" value={money(project.contract_value !== null && project.planned_progress !== null ? project.contract_value * project.planned_progress : null)} note="Planned value" />
        <MiniMetric label="EV" value={money(project.contract_value !== null && project.actual_progress !== null ? project.contract_value * project.actual_progress : null)} note="Earned value" />
        <MiniMetric label="AC" value={money(project.spent_amount)} note="Actual cost / spent" />
        <MiniMetric label="SPI" value={numberValue(project.spi, 2)} note="EV / PV" />
        <MiniMetric label="CPI" value={numberValue(project.cpi, 2)} note="EV / AC" />
      </div>
    );
  }

  if (activeTab === "Contracts") {
    return (
      <div className="workspace-grid">
        <MiniMetric label="Contract Value" value={money(project.contract_value)} note="Current contract value" />
        <MiniMetric label="Paid Amount" value={money(project.paid_amount)} note="Payment file amount" />
        <MiniMetric label="Spent Amount" value={money(project.spent_amount)} note="Actual cost / spent" />
        <MiniMetric label="Remaining" value={money(project.remaining_value)} note="Commercial balance" />
        <MiniMetric label="Contract Rows" value={numberValue(project.source_files.contracts)} note="Contract records" />
        <MiniMetric label="Payment Rows" value={numberValue(project.source_files.payments)} note="Payment records" />
      </div>
    );
  }

  if (activeTab === "Risk Matrix") {
    return (
      <div className="workspace-grid">
        <MiniMetric label="Risk Score" value={numberValue(project.risk_score, 1)} note="Average risk indicator" />
        <MiniMetric label="Risk Records" value={numberValue(project.source_files.risks)} note="Risk rows loaded" />
        <MiniMetric label="Decision Required" value={project.decision_required ? "Yes" : "No"} note="Rule-based management trigger" />
        <MiniMetric label="Delay Days" value={numberValue(project.delay_days)} note="Delay exposure" />
      </div>
    );
  }

  if (activeTab === "Letters Intelligence") {
    return (
      <div className="workspace-two">
        <div>
          <h3>Letters Intelligence</h3>
          <p>Correspondence is project-isolated. The website shows availability and links to the generated project output package where correspondence intelligence is represented.</p>
          <DataStatus label="Claims Rows" count={project.source_files.claims} />
          <DataStatus label="Delay Events" count={project.source_files.delay_events} />
        </div>
        <iframe src={project.reports.master_dashboard} title={`${project.project_display_name} letters intelligence`} />
      </div>
    );
  }

  if (activeTab === "Delay Analysis") {
    return (
      <div className="workspace-two">
        <div>
          <h3>Delay Analysis - Time Impact Analysis</h3>
          <p>Selected project delay logic is shown from the project-specific generated outputs and source registers. No fallback project data is used.</p>
          <DataStatus label="Delay Events" count={project.source_files.delay_events} />
          <DataStatus label="Activities" count={project.source_files.activities} />
        </div>
        <iframe src={project.reports.elite_svg_charts} title={`${project.project_display_name} delay analysis charts`} />
      </div>
    );
  }

  if (activeTab === "Contract & Claims") {
    return (
      <div className="workspace-grid">
        <MiniMetric label="Claims / EOT Exposure" value={money(project.claims_exposure)} note="Claims and EOT source exposure" />
        <MiniMetric label="Claims Rows" value={numberValue(project.source_files.claims)} note="Claims records loaded" />
        <MiniMetric label="Contracts Rows" value={numberValue(project.source_files.contracts)} note="Contract source rows" />
        <MiniMetric label="Evidence Readiness" value={`${numberValue(project.data_quality, 1)}%`} note="Source completeness indicator" />
      </div>
    );
  }

  return (
    <section className="glass-panel report-hologram output-studio-panel">
      <div className="section-header">
        <div>
          <p className="eyebrow">Output Studio</p>
          <h2>{project.project_display_name}</h2>
        </div>
        <span>Same-page generated outputs</span>
      </div>
      <div className="report-switcher">
        {reportTabs.map((tab) => (
          <button
            type="button"
            key={tab.key}
            className={tab.key === selectedReport ? "report-tab active" : "report-tab"}
            onClick={() => setSelectedReport(tab.key)}
          >
            <b>{tab.label}</b>
            <span>{tab.note}</span>
          </button>
        ))}
      </div>
      <iframe src={project.reports[selectedReport]} title={`${project.project_display_name} - ${selectedReport}`} />
    </section>
  );
}

function ProjectWorkspace({
  project,
  selectedReport,
  setSelectedReport
}: {
  project: ProjectRecord;
  selectedReport: ReportKey;
  setSelectedReport: (key: ReportKey) => void;
}) {
  const [activeTab, setActiveTab] = useState<WorkspaceTab>("Overview");
  return (
    <section className="project-workspace">
      <div className="section-header">
        <div>
          <p className="eyebrow">Project Workspace</p>
          <h2>{project.project_display_name}</h2>
        </div>
        <span>{project.sector} / {project.project_folder_name}</span>
      </div>
      <div className="workspace-tabs" role="tablist" aria-label="Project workspace tabs">
        {workspaceTabs.map((tab) => (
          <button
            type="button"
            key={tab}
            className={tab === activeTab ? "workspace-tab active" : "workspace-tab"}
            onClick={() => setActiveTab(tab)}
          >
            {tab}
          </button>
        ))}
      </div>
      <div className="workspace-content">
        <WorkspaceTabContent
          project={project}
          activeTab={activeTab}
          selectedReport={selectedReport}
          setSelectedReport={setSelectedReport}
        />
      </div>
    </section>
  );
}

export default function HomePage() {
  const [selectedProjectKey, setSelectedProjectKey] = useState(projects[0]?.project_key ?? "");
  const [selectedReport, setSelectedReport] = useState<ReportKey>("executive_dashboard");
  const selectedProject = useMemo(
    () => projects.find((project) => project.project_key === selectedProjectKey) ?? projects[0],
    [selectedProjectKey]
  );

  return (
    <main className="future-shell">
      <section className="future-hero">
        <div className="hero-copy">
          <p className="eyebrow">Decision Making Dashboard</p>
          <h1>Decision Making Dashboard</h1>
          <p>
            Portfolio decision view opens first. Choose a project from the dropdown to load the full old-style
            project workspace tabs below in the same page.
          </p>
        </div>
        <label className="holo-select">
          <span>Active Project</span>
          <select value={selectedProjectKey} onChange={(event) => setSelectedProjectKey(event.target.value)}>
            {projects.map((project) => (
              <option value={project.project_key} key={project.project_key}>
                {project.project_display_name}
              </option>
            ))}
          </select>
          <small>Changing this dropdown updates all panels below in the same page.</small>
        </label>
      </section>

      <section className="holo-kpi-grid">
        <HoloKpi title="Projects" value={numberValue(portfolio.project_count)} note={`${portfolio.sector_count} sectors recognized`} tone="cyan" />
        <HoloKpi title="Portfolio Value" value={money(totals.contract_value)} note="Aggregated contract value" tone="gold" />
        <HoloKpi title="Average Progress" value={percent(totals.average_progress)} note="Weighted where possible" tone="green" />
        <HoloKpi title="Average SPI" value={numberValue(totals.average_spi, 2)} note="Portfolio schedule signal" tone={statusTone(totals.average_spi) as "good" | "watch" | "critical" | "neutral"} />
        <HoloKpi title="Average CPI" value={numberValue(totals.average_cpi, 2)} note="Portfolio cost signal" tone={statusTone(totals.average_cpi) as "good" | "watch" | "critical" | "neutral"} />
        <HoloKpi title="Decisions" value={numberValue(totals.decisions_required)} note="Management action triggers" tone={totals.decisions_required > 0 ? "red" : "green"} />
      </section>

      <section className="command-tabs">
        <input id="deck-command" name="deck-tab" type="radio" defaultChecked />
        <input id="deck-sectors" name="deck-tab" type="radio" />
        <input id="deck-projects" name="deck-tab" type="radio" />
        <input id="deck-reports" name="deck-tab" type="radio" />
        <div className="deck-labels">
          <label htmlFor="deck-command">Command Deck</label>
          <label htmlFor="deck-sectors">Sector Matrix</label>
          <label htmlFor="deck-projects">Projects Console</label>
          <label htmlFor="deck-reports">Report Viewer</label>
        </div>

        <div className="deck-panels">
          <section id="command-panel" className="deck-panel">
            <div className="twin-grid">
              <article className="glass-panel digital-map">
                <div className="section-header">
                  <div>
                    <p className="eyebrow">Interactive Network</p>
                    <h2>Project Digital Twin</h2>
                  </div>
                  <span>{selectedProject.project_folder_name}</span>
                </div>
                <ProjectNetwork selectedProject={selectedProject} />
              </article>
              <article className="glass-panel neural-console">
                <div className="section-header">
                  <div>
                    <p className="eyebrow">Performance Signals</p>
                    <h2>Neural Console</h2>
                  </div>
                  <span>{selectedProject.status}</span>
                </div>
                <div className="gauge-grid">
                  <Gauge label="SPI" value={selectedProject.spi} tone={statusTone(selectedProject.spi)} />
                  <Gauge label="CPI" value={selectedProject.cpi} tone={statusTone(selectedProject.cpi)} />
                  <Gauge label="Progress" value={selectedProject.actual_progress} tone="cyan" />
                </div>
                <SignalBar label="Planned progress" value={selectedProject.planned_progress} tone="gold" />
                <SignalBar label="Actual progress" value={selectedProject.actual_progress} tone="cyan" />
                <SignalBar label="Data quality" value={(selectedProject.data_quality ?? 0) / 100} tone="violet" />
              </article>
            </div>
          </section>

          <section id="sectors-panel" className="deck-panel">
            <div className="sector-future-grid">
              {sectors.map((sector) => (
                <article className="glass-panel sector-orb" key={sector.sector}>
                  <h2>{sector.sector}</h2>
                  <div className="orb-value">{sector.project_count}</div>
                  <SignalBar label="Progress" value={sector.average_progress} tone="cyan" />
                  <SignalBar label="SPI" value={sector.average_spi} tone={statusTone(sector.average_spi)} />
                  <SignalBar label="CPI" value={sector.average_cpi} tone={statusTone(sector.average_cpi)} />
                  <div className="metric-row"><span>Budget</span><b>{money(sector.contract_value)}</b></div>
                  <div className="metric-row"><span>Decisions</span><b>{sector.decisions_required}</b></div>
                </article>
              ))}
            </div>
          </section>

          <section id="projects-panel" className="deck-panel">
            <ProjectConsole selectedProject={selectedProject} />
            <div className="project-strip">
              {projects.map((project) => (
                <button
                  type="button"
                  className={project.project_key === selectedProject.project_key ? "project-chip active" : "project-chip"}
                  key={project.project_key}
                  onClick={() => setSelectedProjectKey(project.project_key)}
                >
                  <b>{project.project_folder_name}</b>
                  <span>{project.sector} / SPI {numberValue(project.spi, 2)}</span>
                </button>
              ))}
            </div>
          </section>

          <section id="reports-panel" className="deck-panel">
            <section className="glass-panel report-hologram">
              <div className="section-header">
                <div>
                  <p className="eyebrow">Same-Page Outputs</p>
                  <h2>Holographic Report Viewer</h2>
                </div>
                <span>{selectedProject.project_display_name}</span>
              </div>
              <div className="report-switcher">
                {reportTabs.map((tab) => (
                  <button
                    type="button"
                    key={tab.key}
                    className={tab.key === selectedReport ? "report-tab active" : "report-tab"}
                    onClick={() => setSelectedReport(tab.key)}
                  >
                    <b>{tab.label}</b>
                    <span>{tab.note}</span>
                  </button>
                ))}
              </div>
              <iframe src={selectedProject.reports[selectedReport]} title={`${selectedProject.project_display_name} - ${selectedReport}`} />
            </section>
          </section>
        </div>
      </section>

      <ProjectWorkspace project={selectedProject} selectedReport={selectedReport} setSelectedReport={setSelectedReport} />
      <SourceRegister project={selectedProject} />
    </main>
  );
}
