from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

import os


def generate_executive_summary(df):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    doc = SimpleDocTemplate(
        "reports/executive_summary.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Funnel Analysis Executive Summary",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    total_customers = len(df)

    churned = df[df['Churn'] == 1].shape[0]

    retention = (
        (total_customers - churned)
        / total_customers
    ) * 100

    insights = f"""
    <b>Total Customers:</b> {total_customers}<br/><br/>

    <b>Churned Customers:</b> {churned}<br/><br/>

    <b>Retention Rate:</b> {retention:.2f}%<br/><br/>

    <b>Business Insights</b><br/><br/>

    - Month-to-month customers show higher churn.<br/>
    - Long tenure customers are more loyal.<br/>
    - Higher monthly charges increase churn probability.<br/><br/>

    <b>Recommendations</b><br/><br/>

    - Improve customer retention campaigns.<br/>
    - Introduce loyalty rewards.<br/>
    - Reduce onboarding friction.<br/>
    - Improve customer support quality.<br/>
    """

    paragraph = Paragraph(
        insights,
        styles['BodyText']
    )

    elements.append(paragraph)

    doc.build(elements)

    print("PDF Generated Successfully")