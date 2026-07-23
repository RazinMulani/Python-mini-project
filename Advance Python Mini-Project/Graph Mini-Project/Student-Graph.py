import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English", "Computer", "Physics"]

marks = [85, 78, 92, 88, 81]

study_hours = [2, 3, 4, 5, 6]

students = [
    85, 78, 92, 88, 81,
    65, 70, 74, 69, 83,
    91, 72, 68, 95, 87,
    76, 80, 84, 79, 73
]

fig, ax = plt.subplots(3, 2, figsize=(14, 12))

# 1. LINE GRAPH
ax[0,0].plot(
    subjects,
    marks,
    marker="o",
    linestyle="--",
    color="blue",
    linewidth=2,
    label="Marks"
)

ax[0,0].set_title("Line Graph")
ax[0,0].set_xlabel("Subjects")
ax[0,0].set_ylabel("Marks")
ax[0,0].grid(True)
ax[0,0].legend()

# 2. SCATTER GRAPH
ax[0,1].scatter(
    study_hours,
    marks,
    color="red",
    marker="D",
    s=100,
    label="Study Hours"
)

ax[0,1].set_title("Study Hours vs Marks")
ax[0,1].set_xlabel("Study Hours")
ax[0,1].set_ylabel("Marks")
ax[0,1].grid(True)
ax[0,1].legend()

# 3. BAR CHART
bars = ax[1,0].bar(
    subjects,
    marks,
    color="yellow",
    edgecolor="black",
    width=0.6,
    label="Marks"
)

ax[1,0].set_title("Bar Chart")
ax[1,0].set_xlabel("Subjects")
ax[1,0].set_ylabel("Marks")
ax[1,0].grid(axis="y")
ax[1,0].legend()

# Show values on bars
for bar in bars:
    height = bar.get_height()
    ax[1,0].text(
        bar.get_x() + bar.get_width()/2,
        height + 1,
        str(height),
        ha="center"
    )

# 4. HISTOGRAM
ax[1,1].hist(
    students,
    bins=5,
    color="orange",
    edgecolor="black",
    linewidth=2,
    alpha=0.8,
    label="Students"
)

ax[1,1].set_title("Histogram")
ax[1,1].set_xlabel("Marks")
ax[1,1].set_ylabel("Frequency")
ax[1,1].grid(True)
ax[1,1].legend()

# 5. PIE CHART

colors = ["red", "blue", "green", "orange", "purple"]

explode = [0, 0, 0.1, 0, 0]

ax[2,0].pie(
    marks,
    labels=subjects,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    shadow=True,
    startangle=90
)

ax[2,0].set_title("Marks Percentage")


# 6. HORIZONTAL BAR CHART
ax[2,1].barh(
    subjects,
    marks,
    color="cyan",
    edgecolor="black",
    label="Marks"
)

ax[2,1].set_title("Horizontal Bar Chart")
ax[2,1].set_xlabel("Marks")
ax[2,1].set_ylabel("Subjects")
ax[2,1].grid(axis="x")
ax[2,1].legend()

# MAIN TITLE
fig.suptitle(
    "Student Performance Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout(rect=[0, 0, 1, 0.96])

plt.savefig("Student_Dashboard.png", dpi=300)

plt.show()
