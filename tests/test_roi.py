import unittest

from scripts.estimate_project_roi import estimate_roi


class RoiEstimatorTests(unittest.TestCase):
    def test_standard_automation_pays_back_in_under_4_months(self) -> None:
        report = estimate_roi(
            ops_per_month=100_000,
            manual_hours_saved=40.0,
            hourly_value=35.0,
            setup_fee=4500.0,
        )
        self.assertGreater(report["estimated_monthly_value_usd"]["total_monthly_benefit"], 1500.0)
        self.assertIsNotNone(report["estimated_payback_months"])
        self.assertLess(report["estimated_payback_months"], 4.0)

    def test_high_volume_tier_and_zero_labor_hours(self) -> None:
        report = estimate_roi(ops_per_month=150_000, manual_hours_saved=0.0, hourly_value=50.0, setup_fee=3000.0)
        self.assertEqual(report["estimated_monthly_costs_usd"]["self_hosted_docker_vps"], 60.0)
        self.assertEqual(report["estimated_monthly_value_usd"]["labor_time_savings"], 0.0)
        self.assertGreater(report["estimated_monthly_value_usd"]["saas_license_savings"], 0.0)


if __name__ == "__main__":
    unittest.main()
