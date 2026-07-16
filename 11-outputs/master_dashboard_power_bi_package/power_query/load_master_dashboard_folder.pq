// Change FolderPath to the extracted ZIP data folder.
let
    FolderPath = "C:\\Users\\pc\\OneDrive\\Documents\\Project Intelligence Hub\\11-outputs\\master_dashboard_power_bi_package\\data\\",
    LoadCsv = (FileName as text) => Table.PromoteHeaders(Csv.Document(File.Contents(FolderPath & FileName), [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]), [PromoteAllScalars=true])
in
    [
        Projects = LoadCsv("projects.csv"),
        WBS = LoadCsv("wbs.csv"),
        Activities = LoadCsv("activities.csv"),
        Milestones = LoadCsv("milestones.csv"),
        S_Curve = LoadCsv("s_curve.csv"),
        EVM = LoadCsv("evm.csv"),
        Contracts = LoadCsv("contracts.csv"),
        Payments = LoadCsv("payments.csv"),
        Risks = LoadCsv("risks.csv"),
        Delay_Events = LoadCsv("delay_events.csv"),
        Claims_Summary = LoadCsv("claims_summary.csv"),
        Contract_Clauses = LoadCsv("contract_clauses.csv"),
        Source_Register = LoadCsv("source_file_register.csv")
    ]
