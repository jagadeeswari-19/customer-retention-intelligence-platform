from src.etl.pipeline import run_pipeline


def test_pipeline_execution():

    try:
        run_pipeline()
        assert True

    except Exception:
        assert False