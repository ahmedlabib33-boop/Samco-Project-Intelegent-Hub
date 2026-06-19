"""Central selected-project context used by every project-specific workflow."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class ProjectContext:
    project_id: str
    project_key: str
    project_display_name: str
    project_folder_name: str
    project_folder_path: Path
    is_all_projects: bool
    data_path: Path
    outputs_path: Path
    reports_path: Path
    slides_path: Path
    exports_path: Path
    logs_path: Path
    branding_path: Path
    contracts_path: Path
    contracts_evidence_path: Path
    evidence_path: Path
    notes_path: Path

    @property
    def cache_key(self) -> str:
        try:
            modified_ns = self.project_folder_path.stat().st_mtime_ns
        except OSError:
            modified_ns = 0
        return f"{self.project_id}:{self.project_folder_name}:{modified_ns}"

    def require_project(self, feature_name: str) -> None:
        if self.is_all_projects:
            raise ValueError(f"{feature_name} requires a selected project.")


def build_project_context(record: dict[str, Any] | None, projects_root: Path) -> ProjectContext:
    if not record:
        portfolio_root = projects_root.parent / "generated_outputs" / "portfolio_scope"
        return ProjectContext(
            project_id="",
            project_key="portfolio",
            project_display_name="All Projects",
            project_folder_name="",
            project_folder_path=portfolio_root,
            is_all_projects=True,
            data_path=portfolio_root / "data",
            outputs_path=portfolio_root / "outputs",
            reports_path=portfolio_root / "reports",
            slides_path=portfolio_root / "slides",
            exports_path=portfolio_root / "exports",
            logs_path=portfolio_root / "logs",
            branding_path=portfolio_root / "1-branding",
            contracts_path=portfolio_root / "2-contracts",
            contracts_evidence_path=portfolio_root / "2-contracts" / "evidence",
            evidence_path=portfolio_root / "3-evidence",
            notes_path=portfolio_root / "4-notes",
        )

    folder_path = Path(str(record["project_dir"])).resolve()
    project_id = str(record["project_id"]).strip()
    display_name = str(record.get("project_name") or record.get("project_display_name") or folder_path.name).strip()
    return ProjectContext(
        project_id=project_id,
        project_key=project_id.casefold(),
        project_display_name=display_name,
        project_folder_name=folder_path.name,
        project_folder_path=folder_path,
        is_all_projects=False,
        data_path=folder_path / "data",
        outputs_path=folder_path / "outputs",
        reports_path=folder_path / "reports",
        slides_path=folder_path / "slides",
        exports_path=folder_path / "exports",
        logs_path=folder_path / "logs",
        branding_path=folder_path / "1-branding",
        contracts_path=folder_path / "2-contracts",
        contracts_evidence_path=folder_path / "2-contracts" / "evidence",
        evidence_path=folder_path / "3-evidence",
        notes_path=folder_path / "4-notes",
    )
