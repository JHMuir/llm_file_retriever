import os
from dotenv import load_dotenv
import dspy
from pathlib import Path

from signature import FileRetrieverModule
load_dotenv()

api_key = os.environ["GOOGLE_API_KEY"]

lm = dspy.LM(model="gemini/gemini-2.0-flash", api_key=api_key)
dspy.configure(lm=lm)


module = FileRetrieverModule()

script_dir = Path(__file__).parent
test_dir = script_dir / "test_files"
test_dir.mkdir(exist_ok=True)
(test_dir / "documents").mkdir(exist_ok=True)
(test_dir / "images").mkdir(exist_ok=True)
(test_dir / "documents" / "project_report_q1_2025.pdf").touch()
(test_dir / "documents" / "meeting_notes_april.txt").touch()
(test_dir / "images" / "logo_final.png").touch()
(test_dir / "images" / "graph.jpg").touch()
(test_dir / "archive").mkdir(exist_ok=True) # Empty sub-dir
print(f"\nCreated dummy files in: {test_dir.resolve()}")
print(test_dir)
predict = module(request="Can you get me the project report PDF from Q1?", directory=test_dir)

print(predict)