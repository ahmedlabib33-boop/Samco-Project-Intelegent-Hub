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
  meeting_url?: string | null;
  source_files: Record<string, number>;
  features: FeaturePayload;
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

type FileRecord = {
  name: string;
  relative_path: string;
  extension: string;
  size_kb: number;
  modified: string;
};

type DetectorRecord = {
  name: string;
  status: string;
  detail: string;
};

type TablePreview = {
  file: string;
  exists: boolean;
  row_count: number;
  column_count: number;
  columns: string[];
  rows: Record<string, unknown>[];
};

type XlsxSummary = {
  file: string;
  exists: boolean;
  sheets?: Array<{
    name: string;
    row_count: number;
    column_count: number;
    columns: string[];
    rows: Record<string, unknown>[];
  }>;
  error?: string;
};

type FeaturePayload = {
  overview: {
    data_sources: Record<string, number>;
    source_tables: Record<string, TablePreview>;
  };
  letters_intelligence: {
    folder: string;
    inbox_files: FileRecord[];
    inbox_file_count: number;
    workbook: XlsxSummary;
    detectors: DetectorRecord[];
  };
  delay_analysis: {
    folder: string;
    templates: TablePreview[];
    required_file_count: number;
    recognized_file_count: number;
    missing_required_files: string[];
    schedule_tables: Record<string, TablePreview>;
    detectors: DetectorRecord[];
  };
  contract_claims: {
    folder: string;
    source_files: FileRecord[];
    evidence_files: FileRecord[];
    database: {
      exists: boolean;
      tables: Record<string, number | null>;
      error: string | null;
    };
    clause_library: XlsxSummary;
    detectors: DetectorRecord[];
  };
  outputs_and_watchers: {
    outputs_folder: string;
    output_files: FileRecord[];
    watchers: DetectorRecord[];
  };
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
  "Conference",
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

function displayCell(value: unknown) {
  if (value === null || value === undefined || value === "") return "N/A";
  if (typeof value === "number") return numberValue(value, Number.isInteger(value) ? 0 : 2);
  return String(value);
}

function FeatureSvg({ mode }: { mode: "letters" | "delay" | "claims" | "watcher" | "portfolio" }) {
  const palette = {
    letters: ["#39d7d2", "#63a8ff", "#d6a23a"],
    delay: ["#d6a23a", "#fb7185", "#39d7d2"],
    claims: ["#a78bfa", "#d6a23a", "#63a8ff"],
    watcher: ["#4ade80", "#39d7d2", "#63a8ff"],
    portfolio: ["#39d7d2", "#d6a23a", "#a78bfa"]
  }[mode];
  return (
    <svg className="feature-svg" viewBox="0 0 520 220" role="img" aria-label={`${mode} feature diagram`}>
      <defs>
        <linearGradient id={`grad-${mode}`} x1="0" x2="1" y1="0" y2="1">
          <stop offset="0%" stopColor={palette[0]} />
          <stop offset="55%" stopColor={palette[1]} />
          <stop offset="100%" stopColor={palette[2]} />
        </linearGradient>
        <filter id={`soft-${mode}`}>
          <feGaussianBlur stdDeviation="4" result="blur" />
          <feMerge>
            <feMergeNode in="blur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>
      <rect x="18" y="22" width="484" height="176" rx="28" fill="rgba(4,13,24,.72)" stroke={`url(#grad-${mode})`} />
      <path d="M60 150 C130 42 210 166 275 86 S390 56 455 118" fill="none" stroke={`url(#grad-${mode})`} strokeWidth="8" strokeLinecap="round" filter={`url(#soft-${mode})`} />
      {[70, 180, 290, 405].map((x, index) => (
        <g key={x}>
          <circle cx={x} cy={index % 2 ? 76 : 144} r="22" fill={palette[index % palette.length]} filter={`url(#soft-${mode})`} />
          <circle cx={x} cy={index % 2 ? 76 : 144} r="8" fill="#06101e" />
        </g>
      ))}
      <text x="44" y="58" fill="#f4fbff" fontSize="18" fontWeight="800">{mode.toUpperCase()}</text>
      <text x="44" y="180" fill="#9bb8ca" fontSize="13">Project-scoped detector and analytics flow</text>
    </svg>
  );
}

function DetectorGrid({ detectors }: { detectors: DetectorRecord[] }) {
  return (
    <div className="detector-grid">
      {detectors.map((detector) => (
        <article className="detector-card" key={detector.name}>
          <span className={detector.status.toLowerCase().includes("missing") || detector.status.toLowerCase().includes("needs") ? "detector-badge alert" : "detector-badge"}>
            {detector.status}
          </span>
          <h3>{detector.name}</h3>
          <p>{detector.detail}</p>
        </article>
      ))}
    </div>
  );
}

function FileList({ title, files, emptyText = "No files detected" }: { title: string; files: FileRecord[]; emptyText?: string }) {
  return (
    <section className="feature-card">
      <div className="feature-card-head">
        <h3>{title}</h3>
        <span>{files.length} files</span>
      </div>
      {files.length === 0 ? (
        <p className="empty-note">{emptyText}</p>
      ) : (
        <div className="file-list">
          {files.slice(0, 14).map((file) => (
            <div key={file.relative_path}>
              <b>{file.name}</b>
              <span>{file.extension.toUpperCase()} / {numberValue(file.size_kb, 1)} KB / {file.modified}</span>
            </div>
          ))}
        </div>
      )}
    </section>
  );
}

function TablePreviewPanel({ table, title }: { table: TablePreview | undefined; title?: string }) {
  if (!table || !table.exists) {
    return (
      <section className="feature-card">
        <div className="feature-card-head"><h3>{title || "Table Preview"}</h3><span>Missing</span></div>
        <p className="empty-note">No source table detected for this selected project.</p>
      </section>
    );
  }
  const columns = table.columns.slice(0, 8);
  return (
    <section className="feature-card table-preview-card">
      <div className="feature-card-head">
        <h3>{title || table.file}</h3>
        <span>{table.row_count} rows / {table.column_count} cols</span>
      </div>
      <div className="table-scroll">
        <table>
          <thead>
            <tr>{columns.map((column) => <th key={column}>{column}</th>)}</tr>
          </thead>
          <tbody>
            {table.rows.slice(0, 6).map((row, index) => (
              <tr key={index}>
                {columns.map((column) => <td key={column}>{displayCell(row[column])}</td>)}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

function TemplateInventory({ templates }: { templates: TablePreview[] }) {
  return (
    <section className="feature-card">
      <div className="feature-card-head">
        <h3>Recognized TIA Template Files</h3>
        <span>{templates.length} files</span>
      </div>
      <div className="template-grid">
        {templates.map((template) => (
          <div key={template.file}>
            <b>{template.file}</b>
            <span>{template.row_count} rows / {template.column_count} columns</span>
          </div>
        ))}
      </div>
    </section>
  );
}

function WorkbookSummary({ workbook, title }: { workbook: XlsxSummary; title: string }) {
  return (
    <section className="feature-card">
      <div className="feature-card-head">
        <h3>{title}</h3>
        <span>{workbook.exists ? `${workbook.sheets?.length || 0} sheets` : "Missing"}</span>
      </div>
      {!workbook.exists ? <p className="empty-note">Workbook not available for this project.</p> : null}
      {workbook.error ? <p className="empty-note">{workbook.error}</p> : null}
      <div className="template-grid">
        {(workbook.sheets || []).map((sheet) => (
          <div key={sheet.name}>
            <b>{sheet.name}</b>
            <span>{sheet.row_count} rows / {sheet.column_count} columns</span>
          </div>
        ))}
      </div>
    </section>
  );
}

function ConferencePanel({ project }: { project: ProjectRecord }) {
  const meetingUrl = project.meeting_url?.trim();
  const canEmbed = Boolean(meetingUrl && !meetingUrl.includes("teams.microsoft.com") && !meetingUrl.includes("zoom.us"));
  return (
    <div className="feature-stack">
      <div className="workspace-two">
        <div>
          <h3>Conference Call</h3>
          <p>
            Use this panel during review meetings while the project tabs remain available on the same page.
            The call link is project-specific and can be changed in the selected project `project.json`.
          </p>
          <DataStatus label="Meeting Link" count={meetingUrl ? 1 : 0} />
          <DataStatus label="Project Tabs Available" count={workspaceTabs.length} />
        </div>
        <section className="conference-card">
          <FeatureSvg mode="watcher" />
          <div className="conference-actions">
            {meetingUrl ? (
              <a href={meetingUrl} target="_blank" rel="noreferrer">Join Conference</a>
            ) : (
              <span>Add `meeting_url` to this project's `project.json` to activate the join button.</span>
            )}
          </div>
        </section>
      </div>
      {meetingUrl && canEmbed ? (
        <iframe className="wide-embed conference-embed" src={meetingUrl} title={`${project.project_display_name} conference`} />
      ) : (
        <section className="feature-card">
          <div className="feature-card-head">
            <h3>Same-Page Meeting Setup</h3>
            <span>{meetingUrl ? "External Join" : "Not Configured"}</span>
          </div>
          <p>
            Teams and Zoom usually block iframe embedding for security, so the dashboard keeps the project visible
            and opens the meeting in a controlled new browser tab when required. Google Meet links may also require
            account permission before joining.
          </p>
        </section>
      )}
    </div>
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
      <div className="feature-stack">
        <div className="workspace-grid">
          <MiniMetric label="Project" value={project.project_folder_name} note={project.project_display_name} />
          <MiniMetric label="Status" value={project.status} note={`${project.sector} sector`} />
          <MiniMetric label="Contract Value" value={money(project.contract_value)} note="Project source value" />
          <MiniMetric label="Remaining Value" value={money(project.remaining_value)} note="Contract less paid/spent" />
          <MiniMetric label="Planned Progress" value={percent(project.planned_progress)} note="Planned progress source" />
          <MiniMetric label="Actual Progress" value={percent(project.actual_progress)} note="Actual progress source" />
        </div>
        <div className="workspace-two">
          <FeatureSvg mode="portfolio" />
          <TablePreviewPanel table={project.features.overview.source_tables.projects} title="Project Overview Source" />
        </div>
      </div>
    );
  }

  if (activeTab === "EBS / WBS") {
    return (
      <div className="feature-stack">
        <div className="workspace-grid">
          <MiniMetric label="WBS Rows" value={numberValue(project.features.overview.source_tables.wbs?.row_count)} note="Work breakdown records" />
          <MiniMetric label="Activity Rows" value={numberValue(project.source_files.activities)} note="Activity records linked to WBS" />
          <MiniMetric label="Project Scope" value={project.sector} note="Sector-based project grouping" />
        </div>
        <div className="workspace-two">
          <TablePreviewPanel table={project.features.overview.source_tables.wbs} title="EBS / WBS Source Table" />
          <iframe src={project.reports.master_dashboard} title={`${project.project_display_name} master dashboard WBS`} />
        </div>
      </div>
    );
  }

  if (activeTab === "Activities") {
    return (
      <div className="feature-stack">
        <div className="workspace-grid">
          <MiniMetric label="Activities Loaded" value={numberValue(project.activity_count)} note="Activity source records" />
          <MiniMetric label="Progress Records" value={numberValue(project.source_files.progress)} note="Progress update rows" />
          <MiniMetric label="EVM Records" value={numberValue(project.source_files.evm)} note="Earned value rows" />
          <MiniMetric label="Delay Events" value={numberValue(project.source_files.delay_events)} note="Delay event records" />
        </div>
        <TablePreviewPanel table={project.features.overview.source_tables.activities} title="Activities Register Preview" />
      </div>
    );
  }

  if (activeTab === "Milestones") {
    return (
      <div className="feature-stack">
        <div className="workspace-grid">
          <MiniMetric label="Milestones" value={numberValue(project.milestone_count)} note="Milestone records loaded" />
          <MiniMetric label="Schedule Health" value={numberValue(project.spi, 2)} note="SPI schedule indicator" />
          <MiniMetric label="Delayed Days" value={numberValue(project.delay_days)} note="Delay days from project data" />
        </div>
        <TablePreviewPanel table={project.features.overview.source_tables.milestones} title="Milestone Register Preview" />
      </div>
    );
  }

  if (activeTab === "S-Curve") {
    return (
      <div className="workspace-two">
        <div>
          <h3>S-Curve</h3>
          <p>Uses the selected project progress and generated dashboard outputs. If the source S-curve file is missing, the report remains available with controlled source notes.</p>
          <DataStatus label="S-Curve Rows" count={project.features.overview.source_tables.s_curve?.row_count} />
          <DataStatus label="Progress Updates" count={project.source_files.progress} />
          <TablePreviewPanel table={project.features.overview.source_tables.s_curve} title="S-Curve Source" />
        </div>
        <iframe src={project.reports.linked_executive_dashboard} title={`${project.project_display_name} linked dashboard`} />
      </div>
    );
  }

  if (activeTab === "EVM") {
    return (
      <div className="feature-stack">
        <div className="workspace-grid">
          <MiniMetric label="BAC" value={money(project.contract_value)} note="Budget at completion" />
          <MiniMetric label="PV" value={money(project.contract_value !== null && project.planned_progress !== null ? project.contract_value * project.planned_progress : null)} note="Planned value" />
          <MiniMetric label="EV" value={money(project.contract_value !== null && project.actual_progress !== null ? project.contract_value * project.actual_progress : null)} note="Earned value" />
          <MiniMetric label="AC" value={money(project.spent_amount)} note="Actual cost / spent" />
          <MiniMetric label="SPI" value={numberValue(project.spi, 2)} note="EV / PV" />
          <MiniMetric label="CPI" value={numberValue(project.cpi, 2)} note="EV / AC" />
        </div>
        <TablePreviewPanel table={project.features.overview.source_tables.evm} title="EVM Source Table" />
      </div>
    );
  }

  if (activeTab === "Contracts") {
    return (
      <div className="feature-stack">
        <div className="workspace-grid">
          <MiniMetric label="Contract Value" value={money(project.contract_value)} note="Current contract value" />
          <MiniMetric label="Paid Amount" value={money(project.paid_amount)} note="Payment file amount" />
          <MiniMetric label="Spent Amount" value={money(project.spent_amount)} note="Actual cost / spent" />
          <MiniMetric label="Remaining" value={money(project.remaining_value)} note="Commercial balance" />
          <MiniMetric label="Contract Rows" value={numberValue(project.source_files.contracts)} note="Contract records" />
          <MiniMetric label="Payment Rows" value={numberValue(project.source_files.payments)} note="Payment records" />
        </div>
        <div className="workspace-two">
          <TablePreviewPanel table={project.features.overview.source_tables.contracts} title="Contracts Register Preview" />
          <TablePreviewPanel table={project.features.overview.source_tables.payments} title="Payments Register Preview" />
        </div>
      </div>
    );
  }

  if (activeTab === "Risk Matrix") {
    return (
      <div className="feature-stack">
        <div className="workspace-grid">
          <MiniMetric label="Risk Score" value={numberValue(project.risk_score, 1)} note="Average risk indicator" />
          <MiniMetric label="Risk Records" value={numberValue(project.source_files.risks)} note="Risk rows loaded" />
          <MiniMetric label="Decision Required" value={project.decision_required ? "Yes" : "No"} note="Rule-based management trigger" />
          <MiniMetric label="Delay Days" value={numberValue(project.delay_days)} note="Delay exposure" />
        </div>
        <TablePreviewPanel table={project.features.overview.source_tables.risks} title="Risk Matrix Source Table" />
      </div>
    );
  }

  if (activeTab === "Letters Intelligence") {
    return (
      <div className="feature-stack">
        <div className="workspace-two">
          <div>
            <h3>Letters Intelligence</h3>
            <p>Correspondence is project-isolated. New letters added inside this project's inbox folder are recognized by the generator and reflected after sync/deploy.</p>
            <DataStatus label="Inbox Files" count={project.features.letters_intelligence.inbox_file_count} />
            <DataStatus label="Claims Rows" count={project.source_files.claims} />
            <DataStatus label="Delay Events" count={project.source_files.delay_events} />
          </div>
          <FeatureSvg mode="letters" />
        </div>
        <DetectorGrid detectors={project.features.letters_intelligence.detectors} />
        <div className="workspace-two">
          <WorkbookSummary workbook={project.features.letters_intelligence.workbook} title="Letters Intelligence Workbook" />
          <FileList title="Detected Letter Files" files={project.features.letters_intelligence.inbox_files} />
        </div>
        <iframe className="wide-embed" src={project.reports.master_dashboard} title={`${project.project_display_name} letters intelligence`} />
      </div>
    );
  }

  if (activeTab === "Delay Analysis") {
    return (
      <div className="feature-stack">
        <div className="workspace-two">
          <div>
            <h3>Delay Analysis - Time Impact Analysis</h3>
            <p>Shows upload recognition, template inventory, schedule inputs, MEP support tables, question data, and generated delay outputs for the selected project only.</p>
            <DataStatus label="Recognized TIA Files" count={project.features.delay_analysis.recognized_file_count} />
            <DataStatus label="Required TIA Files" count={project.features.delay_analysis.required_file_count} />
            <DataStatus label="Delay Events" count={project.source_files.delay_events} />
          </div>
          <FeatureSvg mode="delay" />
        </div>
        <DetectorGrid detectors={project.features.delay_analysis.detectors} />
        {project.features.delay_analysis.missing_required_files.length ? (
          <section className="feature-card warning-card">
            <div className="feature-card-head"><h3>Missing Required TIA Files</h3><span>{project.features.delay_analysis.missing_required_files.length}</span></div>
            <p>{project.features.delay_analysis.missing_required_files.join(", ")}</p>
          </section>
        ) : null}
        <TemplateInventory templates={project.features.delay_analysis.templates} />
        <div className="workspace-two">
          <TablePreviewPanel table={project.features.delay_analysis.schedule_tables["MEP Activities"]} title="MEP Activities" />
          <TablePreviewPanel table={project.features.delay_analysis.schedule_tables["MEP Schedule"]} title="MEP Schedule" />
        </div>
        <div className="workspace-two">
          <TablePreviewPanel table={project.features.delay_analysis.schedule_tables["MEP Civil Logic"]} title="MEP Civil Logic" />
          <TablePreviewPanel table={project.features.delay_analysis.schedule_tables["BL Schedule"]} title="BL Schedule" />
        </div>
        <iframe className="wide-embed" src={project.reports.elite_svg_charts} title={`${project.project_display_name} delay analysis charts`} />
      </div>
    );
  }

  if (activeTab === "Contract & Claims") {
    return (
      <div className="feature-stack">
        <div className="workspace-two">
          <div>
            <h3>Contract & Claims Intelligence Center</h3>
            <p>Uses the selected project's contract source folder, evidence folder, and project-specific SQLite knowledge base. It does not read another project's claim library.</p>
            <DataStatus label="Contract Files" count={project.features.contract_claims.source_files.length} />
            <DataStatus label="Evidence Files" count={project.features.contract_claims.evidence_files.length} />
            <DataStatus label="Knowledge Tables" count={Object.keys(project.features.contract_claims.database.tables || {}).length} />
          </div>
          <FeatureSvg mode="claims" />
        </div>
        <div className="workspace-grid">
          <MiniMetric label="Claims / EOT Exposure" value={money(project.claims_exposure)} note="Claims and EOT source exposure" />
          <MiniMetric label="Claims Rows" value={numberValue(project.source_files.claims)} note="Claims records loaded" />
          <MiniMetric label="Contracts Rows" value={numberValue(project.source_files.contracts)} note="Contract source rows" />
          <MiniMetric label="Evidence Readiness" value={`${numberValue(project.data_quality, 1)}%`} note="Source completeness indicator" />
        </div>
        <DetectorGrid detectors={project.features.contract_claims.detectors} />
        <div className="workspace-two">
          <WorkbookSummary workbook={project.features.contract_claims.clause_library} title="Overall Contract Clause Library" />
          <section className="feature-card">
            <div className="feature-card-head"><h3>Knowledge Base Tables</h3><span>{project.features.contract_claims.database.exists ? "SQLite" : "Missing"}</span></div>
            <div className="template-grid">
              {Object.entries(project.features.contract_claims.database.tables || {}).map(([table, count]) => (
                <div key={table}><b>{table}</b><span>{count ?? "N/A"} rows</span></div>
              ))}
            </div>
          </section>
        </div>
        <div className="workspace-two">
          <FileList title="Contract Source Files" files={project.features.contract_claims.source_files} />
          <FileList title="Evidence Files" files={project.features.contract_claims.evidence_files} />
        </div>
      </div>
    );
  }

  if (activeTab === "Conference") {
    return <ConferencePanel project={project} />;
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
      <DetectorGrid detectors={project.features.outputs_and_watchers.watchers} />
      <FileList title="Automatic HTML Outputs" files={project.features.outputs_and_watchers.output_files} />
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
          <div className="brand-lockup">
            <img src="/assets/logo.png" alt="SAMCO Egypt logo" />
            <div>
              <span>SAMCO Egypt</span>
              <small>Project Intelligence Hub</small>
            </div>
          </div>
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
      <footer className="app-credit">
        Designed &amp; Created | <strong>Engr. Ahmed Labib</strong>
      </footer>
    </main>
  );
}
