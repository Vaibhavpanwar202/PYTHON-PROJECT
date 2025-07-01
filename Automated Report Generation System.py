import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

file_path = "data.csv"

# ✅ Step 1: If file doesn't exist or is empty, create sample data
if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
    sample_data = {
        "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
        "Score": [85, 90, 78, 92, 88]
    }
    pd.DataFrame(sample_data).to_csv(file_path, index=False)
    print("📁 'data.csv' was missing or empty. Sample data has been created.")

# ✅ Step 2: Read the CSV file
data = pd.read_csv(file_path)

# ✅ Step 3: Validate required columns
if 'Name' not in data.columns or 'Score' not in data.columns:
    print("❌ ERROR: 'data.csv' must have 'Name' and 'Score' columns.")
    exit()

# ✅ Step 4: Summary stats
average = data["Score"].mean()
maximum = data["Score"].max()
minimum = data["Score"].min()

# ✅ Step 5: Bar chart
plt.figure(figsize=(10, 5))
plt.bar(data["Name"], data["Score"], color="skyblue")
plt.title("Scores Report")
plt.xlabel("Name")
plt.ylabel("Score")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.close()

# ✅ Step 6: Create PDF report
pdf = canvas.Canvas("report.pdf", pagesize=letter)
pdf.setTitle("Automated Report")

pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(50, 750, "Automated Report")

pdf.setFont("Helvetica", 12)
pdf.drawString(50, 720, f"Average Score: {average:.2f}")
pdf.drawString(50, 700, f"Maximum Score: {maximum}")
pdf.drawString(50, 680, f"Minimum Score: {minimum}")

pdf.drawImage("bar_chart.png", 50, 400, width=500, height=250)
pdf.save()

print("✅ 'report.pdf' generated successfully.")





#data.csv
# Name,Score
# Alice,85
# Bob,90
# Charlie,78
# David,92
# Eva,88
