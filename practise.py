import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import gridspec
from datetime import datetime
from matplotlib.patches import FancyBboxPatch

# Load data
csv_path = r"C:\Users\thapa\Downloads\website_data.csv"
df = pd.read_csv(csv_path)
column_name = 'traffic'
if column_name not in df.columns:
    raise KeyError(f"Column '{column_name}' not found in CSV. Available columns: {list(df.columns)}")
data = df[column_name].values
N = len(data)
snake_length = 20

# Prepare quantile bins for pie/bar
quantiles = pd.qcut(data, 5, labels=[f'Q{i+1}' for i in range(5)])
quantile_counts = quantiles.value_counts().sort_index()

# Prepare for heatmap (rolling correlation with lag)
window = 30
corrs = [np.corrcoef(data[max(0, i-window):i], np.roll(data[max(0, i-window):i], 1))[0,1] if i > window else 0 for i in range(N)]

# Modern style
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 13
plt.rcParams['axes.edgecolor'] = '#bdbdbd'
plt.rcParams['axes.linewidth'] = 1.5

# Gradient background
fig = plt.figure(figsize=(20, 12), facecolor='none')
fig.patch.set_alpha(0)
gs = gridspec.GridSpec(3, 4, figure=fig, wspace=0.35, hspace=0.35)

# Add gradient background
def draw_gradient(fig, color1='#e3f0ff', color2='#f3f6fa'):
    from matplotlib.patches import Rectangle
    ax_bg = fig.add_axes([0, 0, 1, 1], zorder=-1)
    ax_bg.axis('off')
    for i in range(100):
        ax_bg.add_patch(Rectangle((0, i/100), 1, 0.01, color=plt.cm.Blues(0.1 + 0.8*i/100)))
draw_gradient(fig)

axes = [fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[0, 2]),
        fig.add_subplot(gs[1, 0]), fig.add_subplot(gs[1, 1]), fig.add_subplot(gs[1, 2]),
        fig.add_subplot(gs[2, 0]), fig.add_subplot(gs[2, 1]), fig.add_subplot(gs[2, 2]),
        fig.add_subplot(gs[0:2, 3])]  # Heatmap on the right

# 1. Colorful Line + Snake (with glow)
main_ax = axes[0]
cmap = plt.get_cmap('tab20')
colors = cmap(np.linspace(0, 1, N))
for i in range(N-1):
    main_ax.plot([i, i+1], [data[i], data[i+1]], color=colors[i], linewidth=2, alpha=0.8, zorder=1)
# Glow effect
for lw, alpha in zip([10, 6, 3], [0.08, 0.15, 0.25]):
    main_ax.plot(np.arange(N), data, color='#ff1744', linewidth=lw, alpha=alpha, zorder=2)
snake_line, = main_ax.plot([], [], color='#ff1744', linewidth=4, label='Snake', zorder=3)
main_ax.set_title("🚦 Colorful Traffic Line", fontsize=16)
main_ax.set_xlim(-2, N+2)
main_ax.set_ylim(data.min() - 0.5, data.max() + 0.5)
main_ax.legend(loc='upper left', fontsize=11, frameon=False)

# 2. Pie Chart (animated explode)
pie_ax = axes[1]
pie_colors = plt.cm.Set2.colors
pie_wedges, pie_texts, pie_autotexts = pie_ax.pie(
    quantile_counts, labels=quantile_counts.index, autopct='%1.1f%%', startangle=90, colors=pie_colors)
pie_ax.set_title("🍰 Traffic Quantile Distribution", fontsize=16)

# 3. Bar Chart
bar_ax = axes[2]
bar_colors = plt.cm.Pastel2.colors
bars = bar_ax.bar(quantile_counts.index, np.zeros_like(quantile_counts), color=bar_colors)
bar_ax.set_ylim(0, quantile_counts.max()*1.1)
bar_ax.set_title("📊 Quantile Bar Chart", fontsize=16)

# 4. Scatter Plot
scatter_ax = axes[3]
scatter = scatter_ax.scatter([], [], c=[], cmap='plasma', s=60, edgecolor='w', linewidth=0.7)
scatter_ax.set_xlim(0, N)
scatter_ax.set_ylim(data.min() - 0.5, data.max() + 0.5)
scatter_ax.set_title("✨ Animated Scatter", fontsize=16)

# 5. Area Plot
area_ax = axes[4]
area = area_ax.fill_between([], [], color='#90caf9', alpha=0.7)
area_ax.set_xlim(0, N)
area_ax.set_ylim(data.min() - 0.5, data.max() + 0.5)
area_ax.set_title("🌊 Animated Area", fontsize=16)

# 6. Histogram
hist_ax = axes[5]
hist = hist_ax.hist([], bins=20, color='#ffb74d', alpha=0.8)
hist_ax.set_xlim(data.min(), data.max())
hist_ax.set_title("📈 Animated Histogram", fontsize=16)

# 7. Box Plot
box_ax = axes[6]
box = box_ax.boxplot([], patch_artist=True, boxprops=dict(facecolor='#b2dfdb'))
box_ax.set_ylim(data.min() - 0.5, data.max() + 0.5)
box_ax.set_title("📦 Animated Box", fontsize=16)

# 8. Step Plot
step_ax = axes[7]
step_line, = step_ax.step([], [], where='mid', color='#7e57c2', linewidth=2)
step_ax.set_xlim(0, N)
step_ax.set_ylim(data.min() - 0.5, data.max() + 0.5)
step_ax.set_title("📉 Animated Step", fontsize=16)

# 9. Info Panel (rounded box, live stats)
info_ax = axes[8]
info_ax.axis('off')
info_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.9, boxstyle="round,pad=0.1,rounding_size=0.15",
                          linewidth=0, facecolor='#f3f6fa', alpha=0.95, transform=info_ax.transAxes, zorder=0)
info_ax.add_patch(info_box)
info_text = info_ax.text(0.5, 0.5, "Portfolio Demo\nDynamic Data Dashboard", ha='center', va='center',
             fontsize=20, color='#333', fontweight='bold', alpha=0.8, zorder=1)

# 10. Heatmap (Rolling Correlation)
heatmap_ax = axes[9]
heatmap_img = heatmap_ax.imshow(np.zeros((1, N)), aspect='auto', cmap='coolwarm', vmin=-1, vmax=1)
heatmap_ax.set_title("🔥 Rolling Correlation Heatmap", fontsize=16)
heatmap_ax.set_yticks([])
heatmap_ax.set_xticks([])

# Real-time clock
clock_text = fig.text(0.5, 0.98, "", ha='center', va='top', fontsize=18, color='#333', fontweight='bold', alpha=0.9)

def get_clock_str():
    now = datetime.now()
    return now.strftime("%I:%M:%S %p")

def ease_in_out(t):
    return t*t*(3 - 2*t)

def animate(frame):
    t = ease_in_out(frame / (N-1))
    i = int(t * (N-1))

    # Update clock
    clock_text.set_text(get_clock_str())

    # Snake highlight
    start = max(0, i - snake_length + 1)
    x_snake = np.linspace(start, i, snake_length)
    y_snake = np.interp(x_snake, np.arange(N), data)
    snake_line.set_data(x_snake, y_snake)

    # Pie chart: animate explode
    explode_radius = 0.13 + 0.07*np.sin(2*np.pi*frame/60)
    explode = [explode_radius if j == (i // (N//5)) % 5 else 0 for j in range(5)]
    pie_ax.clear()
    pie_ax.pie(quantile_counts, labels=quantile_counts.index, autopct='%1.1f%%',
               startangle=90, colors=pie_colors, explode=explode, textprops={'fontsize':13})
    pie_ax.set_title("🍰 Traffic Quantile Distribution", fontsize=16)

    # Bar chart: animate bar heights
    bar_ax.clear()
    bar_vals = quantile_counts * (i/N)
    bars = bar_ax.bar(quantile_counts.index, bar_vals, color=bar_colors, edgecolor='#888', linewidth=1.2)
    for bar, val in zip(bars, bar_vals):
        bar_ax.text(bar.get_x() + bar.get_width()/2, val + 0.5, f"{int(val)}", ha='center', va='bottom', fontsize=11)
    bar_ax.set_ylim(0, quantile_counts.max()*1.1)
    bar_ax.set_title("📊 Quantile Bar Chart", fontsize=16)

    # Scatter: animate up to frame
    scatter_ax.clear()
    scatter_ax.scatter(np.arange(i+1), data[:i+1], c=data[:i+1], cmap='plasma', s=60, edgecolor='w', linewidth=0.7)
    scatter_ax.set_xlim(0, N)
    scatter_ax.set_ylim(data.min() - 0.5, data.max() + 0.5)
    scatter_ax.set_title("✨ Animated Scatter", fontsize=16)

    # Area: animate up to frame
    area_ax.clear()
    area_ax.fill_between(np.arange(i+1), data[:i+1], color='#90caf9', alpha=0.7)
    area_ax.set_xlim(0, N)
    area_ax.set_ylim(data.min() - 0.5, data.max() + 0.5)
    area_ax.set_title("🌊 Animated Area", fontsize=16)

    # Histogram: animate up to frame
    hist_ax.clear()
    hist_ax.hist(data[:i+1], bins=20, color='#ffb74d', alpha=0.8, edgecolor='#fff')
    hist_ax.set_xlim(data.min(), data.max())
    hist_ax.set_title("📈 Animated Histogram", fontsize=16)

    # Box: animate up to frame
    box_ax.clear()
    if i > 1:
        box_ax.boxplot(data[:i+1], patch_artist=True, boxprops=dict(facecolor='#b2dfdb', linewidth=0))
    box_ax.set_ylim(data.min() - 0.5, data.max() + 0.5)
    box_ax.set_title("📦 Animated Box", fontsize=16)

    # Step: animate up to frame
    step_ax.clear()
    step_ax.step(np.arange(i+1), data[:i+1], where='mid', color='#7e57c2', linewidth=2)
    step_ax.set_xlim(0, N)
    step_ax.set_ylim(data.min() - 0.5, data.max() + 0.5)
    step_ax.set_title("📉 Animated Step", fontsize=16)

    # Info panel: live stats
    info_ax.clear()
    info_ax.axis('off')
    info_box = FancyBboxPatch((0.05, 0.05), 0.9, 0.9, boxstyle="round,pad=0.1,rounding_size=0.15",
                              linewidth=0, facecolor='#f3f6fa', alpha=0.95, transform=info_ax.transAxes, zorder=0)
    info_ax.add_patch(info_box)
    stats = f"Mean: {np.mean(data[:i+1]):.2f}\nStd: {np.std(data[:i+1]):.2f}\nMin: {np.min(data[:i+1]):.2f}\nMax: {np.max(data[:i+1]):.2f}"
    info_ax.text(0.5, 0.7, "Portfolio Demo\nDynamic Data Dashboard", ha='center', va='center',
                 fontsize=20, color='#333', fontweight='bold', alpha=0.85, zorder=1)
    info_ax.text(0.5, 0.35, stats, ha='center', va='center', fontsize=15, color='#555', alpha=0.85, zorder=1)

    # Heatmap: rolling correlation
    heatmap_ax.clear()
    heatmap_ax.imshow(np.array([corrs[:i+1] + [0]*(N-i-1)]), aspect='auto', cmap='coolwarm', vmin=-1, vmax=1)
    heatmap_ax.set_title("🔥 Rolling Correlation Heatmap", fontsize=16)
    heatmap_ax.set_yticks([])
    heatmap_ax.set_xticks([])

    return []

# Highlight effect on hover
highlight_color = '#e3f2fd'
default_color = '#f3f6fa'
for ax in axes:
    ax.set_facecolor(default_color)
    for spine in ax.spines.values():
        spine.set_linewidth(1.5)
        spine.set_edgecolor('#bdbdbd')
        spine.set_capstyle('round')

def on_move(event):
    for ax in axes:
        if ax == event.inaxes:
            ax.set_facecolor(highlight_color)
        else:
            ax.set_facecolor(default_color)
    fig.canvas.draw_idle()

fig.canvas.mpl_connect('motion_notify_event', on_move)

# Stylish watermark
fig.text(0.99, 0.01, "© karl's", fontsize=13, color='#b0b0b0', ha='right', va='bottom', alpha=0.6, fontstyle='italic')

# Faster, smoother animation (interval=15ms)
ani = FuncAnimation(fig, animate, frames=N, interval=8, blit=False)
plt.show()
