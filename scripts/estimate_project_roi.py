"""
Client Automation ROI & Cloud Infrastructure Cost Estimator
"""

import argparse
import json


def estimate_roi(ops_per_month: int, manual_hours_saved: float, hourly_value: float, setup_fee: float) -> dict:
    # Typical Zapier/Make volume cost vs Self-Hosted n8n Docker VPS
    saas_ops_cost = round(max(49.0, (ops_per_month / 1000.0) * 5.5), 2)
    self_hosted_vps = 24.0 if ops_per_month <= 100_000 else 60.0
    llm_api_cost = round((ops_per_month / 1000.0) * 0.45, 2)

    monthly_saas_savings = round(max(0.0, saas_ops_cost - (self_hosted_vps + llm_api_cost)), 2)
    monthly_labor_savings = round(manual_hours_saved * hourly_value, 2)
    total_monthly_value = round(monthly_saas_savings + monthly_labor_savings, 2)
    payback_months = round(setup_fee / total_monthly_value, 2) if total_monthly_value > 0 else None

    return {
        "inputs": {
            "ops_per_month": ops_per_month,
            "manual_hours_saved": manual_hours_saved,
            "hourly_value_usd": hourly_value,
            "setup_fee_usd": setup_fee,
        },
        "estimated_monthly_costs_usd": {
            "traditional_saas_automation": saas_ops_cost,
            "self_hosted_docker_vps": self_hosted_vps,
            "routed_llm_api_usage": llm_api_cost,
        },
        "estimated_monthly_value_usd": {
            "saas_license_savings": monthly_saas_savings,
            "labor_time_savings": monthly_labor_savings,
            "total_monthly_benefit": total_monthly_value,
        },
        "estimated_payback_months": payback_months,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Estimate AI automation ROI & infrastructure costs")
    parser.add_argument("--ops-per-month", type=int, default=100000)
    parser.add_argument("--manual-hours-saved", type=float, default=40.0)
    parser.add_argument("--hourly-value", type=float, default=35.0)
    parser.add_argument("--setup-fee", type=float, default=4500.0)
    args = parser.parse_args()

    print(json.dumps(estimate_roi(args.ops_per_month, args.manual_hours_saved, args.hourly_value, args.setup_fee), indent=2))
