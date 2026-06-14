# Data Dictionary

## projects

Master project record.

- `project_id`: unique project code.
- `name`: project name.
- `client`: employer/client.
- `contractor`: main contractor.
- `baseline_start`: contract baseline start date.
- `baseline_finish`: contract baseline finish date.
- `forecast_finish`: current forecast completion date.
- `contract_value`: approved project value used for high-level EV calculations.
- `currency`: reporting currency.
- `status`: active, closed, suspended, or other local status.

## activities

Planning and progress records.

- `activity_id`: unique system activity ID.
- `activity_code`: planning system activity code.
- `wbs_id`: work breakdown structure link.
- `baseline_start`, `baseline_finish`: approved baseline dates.
- `actual_start`, `actual_finish`: actual dates.
- `forecast_start`, `forecast_finish`: current forecast dates.
- `planned_weight`: weighted contribution to total project progress.
- `planned_progress`: planned percent complete at reporting date.
- `actual_progress`: actual percent complete at reporting date.
- `total_float_days`: float from the current schedule.
- `is_critical`: `1` if critical, `0` if not.

## contracts

Contract package register.

- `contract_id`: unique contract ID.
- `package`: package name.
- `contractor`: supplier, subcontractor, or main contractor.
- `contract_type`: lump sum, re-measurable, design and build, cost plus, etc.
- `original_value`: original contract sum.
- `approved_variations`: approved change value.
- `pending_variations`: submitted or forecast variations not yet approved.
- `paid_to_date`: amount paid.
- `retention_percent`: retention percentage.

## change_orders

Variation and change order register.

- `co_id`: unique change order ID.
- `claimed_amount`: submitted amount.
- `approved_amount`: approved amount.
- `time_impact_days`: claimed or assessed time impact.
- `owner_response_due`: date by which response is due.

## claims

Claims and EOT register.

- `claim_id`: unique claim ID.
- `event_ref`: related delay event if applicable.
- `notice_date`: date notice was issued.
- `particulars_due`: due date for detailed particulars.
- `claimed_amount`: claimed cost.
- `claimed_days`: claimed EOT days.
- `entitlement_basis`: short basis of claim.
- `responsibility`: employer, contractor, shared, authority, or other.

## delay_events

Delay event log.

- `delay_id`: unique delay event ID.
- `start_date`, `end_date`: event window.
- `responsibility`: party responsible for the event.
- `impacted_activity_id`: impacted activity.
- `cause_category`: cause type such as design, authority, productivity, weather, or physical condition.
- `estimated_delay_days`: estimated delay impact.
- `approved_eot_days`: approved extension of time days.

## risks

Risk register.

- `probability`: decimal probability from `0` to `1`.
- `time_impact_days`: possible time impact if risk occurs.
- `cost_impact`: possible cost impact if risk occurs.
- `response_strategy`: mitigation, transfer, avoid, accept, or monitor.
- `owner`: action owner.
- `due_date`: mitigation due date.

