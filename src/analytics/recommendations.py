
def generate_recommendations(metrics):

    recommendations = []

    if metrics["Churn Rate"] > 25:
        recommendations.append(
            "Improve customer retention campaigns"
        )

    if metrics["Retention Rate"] < 70:
        recommendations.append(
            "Offer loyalty discounts"
        )

    return recommendations