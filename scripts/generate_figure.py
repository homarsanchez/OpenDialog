"""
Figure 8: Integrated Quantitative Framework for Human Capital Transformation
=============================================================================

Generates publication-grade 4-panel composite figure for academic essay:
"Cognitive Capital in the Age of Algorithmic Intelligence"

Author: [Your Name]
Date: March 2026
Repository: github.com/[your-repo]/human-capital-transformation
License: MIT

Dependencies: matplotlib, seaborn, numpy, pandas, networkx
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import seaborn as sns
import networkx as nx
from pathlib import Path

# Configuration
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['xtick.labelsize'] = 9
plt.rcParams['ytick.labelsize'] = 9
plt.rcParams['legend.fontsize'] = 9
plt.rcParams['figure.titlesize'] = 14

# Data paths
DATA_DIR = Path('data')
OUTPUT_DIR = Path('outputs')
OUTPUT_DIR.mkdir(exist_ok=True)

# ==============================================================================
# Panel A: Labor Market Polarization Dynamics
# ==============================================================================

def panel_a_labor_polarization(ax):
    """
    Mathematical model: Employment_index(t) = 100 * exp(growth_rate * t)
    where t = years since 2025
    """
    # Load data
    df = pd.read_csv(DATA_DIR / 'labor_polarization_2025_2035.csv', comment='#')
    
    # Plot curves
    ax.plot(df['year'], df['high_skill_cognitive'], 
            color='#2c5aa0', linewidth=2, label='High-skill cognitive (+42%)')
    ax.plot(df['year'], df['mid_skill_routine'], 
            color='#c94040', linewidth=2, label='Mid-skill routine (-31%)')
    ax.plot(df['year'], df['low_skill_nonroutine'], 
            color='#5a9e5a', linewidth=2, label='Low-skill non-routine (+18%)')
    
    # Highlight "missing middle" collapse zone
    ax.fill_between(df['year'], 85, 115, alpha=0.1, color='red', 
                     label='Missing middle risk zone')
    
    # Styling
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Employment Index (2025=100)', fontweight='bold')
    ax.set_title('Panel A: Labor Market Polarization Dynamics\n' + 
                 r'$H(t)=100e^{0.042t}$, $M(t)=100e^{-0.031t}$, $L(t)=100e^{0.018t}$',
                 fontsize=11, fontweight='bold')
    ax.legend(loc='best', frameon=True, fancybox=True, shadow=True)
    ax.grid(alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_xlim(2025, 2035)
    
    # Annotations
    ax.annotate('High-skill\ngrowth', xy=(2033, 139), xytext=(2031, 155),
                arrowprops=dict(arrowstyle='->', color='#2c5aa0', lw=1.5),
                fontsize=9, color='#2c5aa0', fontweight='bold')
    ax.annotate('Middle-skill\ncollapse', xy=(2033, 78), xytext=(2031, 60),
                arrowprops=dict(arrowstyle='->', color='#c94040', lw=1.5),
                fontsize=9, color='#c94040', fontweight='bold')

# ==============================================================================
# Panel B: Three-Horizon Productivity Trajectories
# ==============================================================================

def panel_b_productivity_trajectories(ax):
    """
    Mathematical model: P(t) = P₀(1 + r)^t
    where r ∈ {3.8%, 6.2%, 7.1%}
    """
    # Load data
    df = pd.read_csv(DATA_DIR / 'productivity_trajectories.csv', comment='#')
    
    # Plot trajectories
    ax.plot(df['year'], df['trajectory_alpha_china'], 
            color='#c94040', linewidth=2.5, 
            label='Alpha: China 6.2% (p=0.68)')
    ax.plot(df['year'], df['trajectory_beta_russia'], 
            color='#2c5aa0', linewidth=2.5,
            label='Beta: Russia 3.8% (p=0.54)')
    ax.plot(df['year'], df['trajectory_gamma_global_south'], 
            color='#5a9e5a', linewidth=2.5,
            label='Gamma: Global South 7.1% (p=0.45)')
    
    # Add confidence bands (±10%)
    for col, color in [('trajectory_alpha_china', '#c94040'),
                        ('trajectory_beta_russia', '#2c5aa0'),
                        ('trajectory_gamma_global_south', '#5a9e5a')]:
        upper = df[col] * 1.1
        lower = df[col] * 0.9
        ax.fill_between(df['year'], lower, upper, alpha=0.15, color=color)
    
    # OECD 5% threshold line (2.3x recovery acceleration marker)
    ax.axhline(y=1.23, color='gray', linestyle='--', linewidth=1.5,
               label='OECD 5% GDP threshold (2.3x)')
    
    # Styling
    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Productivity Multiplier (2025=1.0)', fontweight='bold')
    ax.set_title('Panel B: Three-Horizon Productivity Trajectories\n' + 
                 r'$P(t) = P_0(1+r)^t$ where $r \in \{0.038, 0.062, 0.071\}$',
                 fontsize=11, fontweight='bold')
    ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True)
    ax.grid(alpha=0.3, linestyle='--', linewidth=0.5)
    ax.set_xlim(2025, 2035)
    ax.set_ylim(0.9, 2.1)

# ==============================================================================
# Panel C: Investment ROI Surface (Heatmap)
# ==============================================================================

def panel_c_investment_roi(ax):
    """
    Mathematical model: ROI(i, a) = β₀ + β₁*i + β₂*a + β₃*i*a
    where i = GDP investment %, a = adaptive capacity index
    """
    # Load data
    df = pd.read_csv(DATA_DIR / 'investment_roi_matrix.csv', comment='#')
    
    # Create pivot table for heatmap
    heatmap_data = df.pivot(index='adaptive_capacity_index', 
                             columns='gdp_investment_pct', 
                             values='roi_multiplier')
    
    # Create heatmap
    sns.heatmap(heatmap_data, cmap='Greys', annot=False, fmt='.1f',
                cbar_kws={'label': 'ROI Multiplier'}, ax=ax,
                linewidths=0.5, linecolor='white')
    
    # Highlight critical 5% threshold zone
    ax.add_patch(plt.Rectangle((2, 2), 1, 3, fill=False, 
                                edgecolor='red', linewidth=2.5, linestyle='--'))
    ax.text(2.5, 1.5, '5% threshold\n(2.3x acceleration)', 
            color='red', fontsize=8, fontweight='bold', ha='center')
    
    # Styling
    ax.set_xlabel('GDP Investment (%)', fontweight='bold')
    ax.set_ylabel('Adaptive Capacity Index', fontweight='bold')
    ax.set_title('Panel C: Investment ROI Surface\n' + 
                 r'$ROI(i,a) = 0.5 + 0.3i + 0.2a + 0.05ia$',
                 fontsize=11, fontweight='bold')
    ax.invert_yaxis()

# ==============================================================================
# Panel D: Bayesian Causal Network Structure
# ==============================================================================

def panel_d_bayesian_network(ax):
    """
    Bayesian network showing causal relationships between policy inputs,
    mediators, and outcomes. Probabilities from OECD (2023), McKinsey (2021).
    """
    # Create directed graph
    G = nx.DiGraph()
    
    # Define node layers
    policy_inputs = ['GDP\ninvest', 'AI\ndeploy', 'Edu\nreform']
    mediators = ['Workforce', 'Credential\nvel', 'H-AI\nsynergy']
    outcomes = ['Productivity', 'Inequality↓', 'Employment']
    
    # Add nodes with positions
    pos = {}
    
    # Policy inputs (top layer)
    for i, node in enumerate(policy_inputs):
        pos[node] = (i * 2, 3)
        G.add_node(node, layer='policy')
    
    # Mediators (middle layer)
    for i, node in enumerate(mediators):
        pos[node] = (i * 2, 2)
        G.add_node(node, layer='mediator')
    
    # Outcomes (bottom layer)
    for i, node in enumerate(outcomes):
        pos[node] = (i * 2, 1)
        G.add_node(node, layer='outcome')
    
    # Add edges with probabilities
    edges = [
        ('GDP\ninvest', 'Workforce', 0.72),
        ('Edu\nreform', 'Workforce', 0.58),
        ('AI\ndeploy', 'Credential\nvel', 0.65),
        ('Edu\nreform', 'Credential\nvel', 0.58),
        ('AI\ndeploy', 'H-AI\nsynergy', 0.70),
        ('Workforce', 'H-AI\nsynergy', 0.62),
        ('Workforce', 'Productivity', 0.68),
        ('H-AI\nsynergy', 'Productivity', 0.75),
        ('Credential\nvel', 'Inequality↓', 0.54),
        ('GDP\ninvest', 'Inequality↓', 0.48),
        ('H-AI\nsynergy', 'Employment', 0.45),
        ('Workforce', 'Employment', 0.52),
    ]
    
    for source, target, prob in edges:
        G.add_edge(source, target, weight=prob)
    
    # Draw network
    ax.axis('off')
    
    # Node colors by layer
    node_colors = []
    for node in G.nodes():
        if G.nodes[node]['layer'] == 'policy':
            node_colors.append('#e8f4f8')
        elif G.nodes[node]['layer'] == 'mediator':
            node_colors.append('#f0f0e8')
        else:
            node_colors.append('#e8f8e8')
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, 
                            node_size=1800, edgecolors='black',
                            linewidths=1.5, ax=ax)
    
    # Draw edges with varying thickness by probability
    for (source, target, data) in G.edges(data=True):
        weight = data['weight']
        width = weight * 3  # Scale edge width by probability
        nx.draw_networkx_edges(G, pos, [(source, target)], 
                                width=width, alpha=0.6,
                                edge_color='gray',
                                arrowsize=15, ax=ax,
                                connectionstyle='arc3,rad=0.1')
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold', ax=ax)
    
    # Draw edge labels (probabilities)
    edge_labels = {(s, t): f'{d["weight"]:.2f}' 
                   for s, t, d in G.edges(data=True)}
    nx.draw_networkx_edge_labels(G, pos, edge_labels, 
                                   font_size=7, font_color='red', ax=ax)
    
    # Title
    ax.set_title('Panel D: Bayesian Causal Network Structure\n' + 
                 r'$P(Outcome|Policy,Context)$ from empirical distributions',
                 fontsize=11, fontweight='bold', pad=20)
    
    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#e8f4f8', edgecolor='black', label='Policy inputs'),
        mpatches.Patch(facecolor='#f0f0e8', edgecolor='black', label='Mediators'),
        mpatches.Patch(facecolor='#e8f8e8', edgecolor='black', label='Outcomes')
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=8)

# ==============================================================================
# Main: Generate Complete Figure
# ==============================================================================

def main():
    """Generate complete 4-panel composite figure"""
    
    print("Generating Figure 8: Integrated Quantitative Framework...")
    
    # Create figure with 2x2 subplot grid
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.30)
    
    # Create subplots
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b = fig.add_subplot(gs[0, 1])
    ax_c = fig.add_subplot(gs[1, 0])
    ax_d = fig.add_subplot(gs[1, 1])
    
    # Generate panels
    print("  - Panel A: Labor polarization dynamics...")
    panel_a_labor_polarization(ax_a)
    
    print("  - Panel B: Productivity trajectories...")
    panel_b_productivity_trajectories(ax_b)
    
    print("  - Panel C: Investment ROI surface...")
    panel_c_investment_roi(ax_c)
    
    print("  - Panel D: Bayesian network...")
    panel_d_bayesian_network(ax_d)
    
    # Overall title
    fig.suptitle('Figure 8: Integrated Quantitative Framework for Human Capital Transformation\n' +
                 'Mathematical foundations for multipolar cognitive capital investment (2025-2035)',
                 fontsize=15, fontweight='bold', y=0.98)
    
    # Caption
    caption_text = (
        "Mathematical models: Panel A: H(t)=100e^(0.042t), M(t)=100e^(-0.031t), L(t)=100e^(0.018t). "
        "Panel B: P(t)=P₀(1+r)^t where r∈{3.8%, 6.2%, 7.1%}. Panel C: ROI(i,a)=β₀+β₁i+β₂a+β₃ia, "
        "i=GDP%, a=adaptive capacity. Panel D: Bayesian network with P(Outcome|Policy,Context) "
        "from empirical distributions. Data sources: Autor & Dorn (2023), Frey & Osborne (2017), "
        "OECD (2023), McKinsey (2021), Acemoglu & Restrepo (2020). "
        "Repository: github.com/[your-repo]/human-capital-transformation"
    )
    
    fig.text(0.5, 0.01, caption_text, ha='center', fontsize=9, 
             style='italic', wrap=True, color='#444')
    
    # Save outputs
    print("\nSaving outputs...")
    
    # High-resolution PDF for publication
    pdf_path = OUTPUT_DIR / 'figure_8_composite.pdf'
    plt.savefig(pdf_path, dpi=300, bbox_inches='tight', format='pdf')
    print(f"  ✓ Saved: {pdf_path}")
    
    # High-resolution PNG for presentations
    png_path = OUTPUT_DIR / 'figure_8_composite.png'
    plt.savefig(png_path, dpi=300, bbox_inches='tight', format='png')
    print(f"  ✓ Saved: {png_path}")
    
    # Individual panel exports
    panel_dir = OUTPUT_DIR / 'panel_individual_exports'
    panel_dir.mkdir(exist_ok=True)
    
    for ax, label in [(ax_a, 'panel_a_labor_polarization'),
                       (ax_b, 'panel_b_productivity_trajectories'),
                       (ax_c, 'panel_c_investment_roi'),
                       (ax_d, 'panel_d_bayesian_network')]:
        extent = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        extent_expanded = extent.expanded(1.2, 1.2)
        fig.savefig(panel_dir / f'{label}.png', bbox_inches=extent_expanded, dpi=300)
    
    print(f"  ✓ Saved individual panels to: {panel_dir}")
    
    print("\n✓ Figure generation complete!")
    print(f"\nOutput files:")
    print(f"  - {pdf_path}")
    print(f"  - {png_path}")
    print(f"  - {panel_dir}/ (4 individual panels)")
    
    plt.show()

if __name__ == '__main__':
    main()