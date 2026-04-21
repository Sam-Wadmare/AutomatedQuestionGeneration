import pandas as pd

from app import create_app


class FakeGenerator:
    def __call__(self, prompt):
        return [{"generated_text": f"Generated from: {prompt[:20]}"}]


def build_dataframe():
    return pd.DataFrame(
        [
            {
                "Question": "What is 2 + 2?",
                "Option A": "1",
                "Option B": "2",
                "Option C": "3",
                "Option D": "4",
                "Answer": "D",
            }
        ]
    )


def test_home_route_returns_html():
    app = create_app(generator=FakeGenerator(), dataframe=build_dataframe())
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Smart Aptitude AI Question Generator" in response.data


def test_generate_route_response_shape():
    app = create_app(generator=FakeGenerator(), dataframe=build_dataframe())
    client = app.test_client()

    response = client.get("/generate")
    payload = response.get_json()

    assert response.status_code == 200
    assert set(payload.keys()) == {"question", "options", "answer"}
    assert isinstance(payload["question"], str)
    assert isinstance(payload["options"], list)
    assert len(payload["options"]) == 4
    assert isinstance(payload["answer"], str)


def test_csv_required_columns_present():
    df = pd.read_csv("clean_general_aptitude_dataset.csv", sep=";")
    expected = {"Question", "Option A", "Option B", "Option C", "Option D", "Answer"}

    assert expected.issubset(set(df.columns))
