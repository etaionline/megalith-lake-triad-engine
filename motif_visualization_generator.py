#!/usr/bin/env python3
"""
Motif Visualization Generator
Creates publication-quality visualizations for the megalith-lake-triad research
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.patches import Circle, FancyBboxPatch
from matplotlib.colors import LinearSegmentedColormap
import networkx as nx
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import warnings
warnings.filterwarnings('ignore')

# Set style for publication quality
plt.style.use('dark_background')
sns.set_palette("husl")

# Define research colors
COLORS = {
    'megalith': '#38BDF8',
    'civilization': '#A78BFA', 
    'lake': '#34D399',
    'serpent': '#EF4444',
    'energy': '#F59E0B',
    'mythology': '#EC4899'
}

def create_motif_overview():
    """Create overview of 18 mythological motifs"""
    fig, ax = plt.subplots(figsize=(16, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(5, 9.5, 'THE 18 MOTIFS: Global Mythological Patterns', 
            ha='center', va='center', fontsize=24, fontweight='bold', color='white')
    
    # Categories and motifs
    categories = {
        'Serpent & Strike': [
            '1. Serpent Killed by Thunder Weapon',
            '2. Linear Scar on Mountain/Desert', 
            '3. Blood/Tears → Salt Lake',
            '4. Guards Shining Stones',
            '5. Rivers Freed/Lakes Drained'
        ],
        'Directional & Environmental': [
            '6. Name Contains Black/Dark/North',
            '7. Serpent Encircles Lake',
            '8. Thunder Weapon Diamond/Crystal',
            '9. Sky Turned Red Three Days',
            '10. Serpent Body Mountain Ridge'
        ],
        'Divine Intervention': [
            '11. Bird Eagle Garuda Weapon',
            '12. Divine Eye Sees Truth',
            '13. Lightning Splits Sky',
            '14. Underground Voice Commands'
        ],
        'Return & Transformation': [
            '15. Dragon Sleeps Beneath Mountain',
            '16. Wise Old Dragon Returns',
            '17. Dragon Child Inherits Kingdom',
            '18. Cycle Repeats Every Era'
        ]
    }
    
    y_positions = [8, 6.5, 5, 3.5]
    colors = [COLORS['serpent'], COLORS['energy'], COLORS['mythology'], COLORS['megalith']]
    
    for i, (category, motifs) in enumerate(categories.items()):
        y = y_positions[i]
        
        # Category header
        bbox = FancyBboxPatch((0.5, y-0.2), 9, 0.4, 
                            boxstyle="round,pad=0.1", 
                            facecolor=colors[i], alpha=0.3,
                            edgecolor=colors[i], linewidth=2)
        ax.add_patch(bbox)
        
        ax.text(1, y, category, fontsize=16, fontweight='bold', 
               color=colors[i], va='center')
        
        # Motifs
        for j, motif in enumerate(motifs):
            ax.text(1.2, y - 0.3 - j*0.2, motif, fontsize=11, 
                   color='lightgray', va='center')
    
    # Add onomatopoeia pattern box
    ono_bbox = FancyBboxPatch((0.5, 1.5), 9, 1, 
                             boxstyle="round,pad=0.1", 
                             facecolor=COLORS['mythology'], alpha=0.3,
                             edgecolor=COLORS['mythology'], linewidth=2)
    ax.add_patch(ono_bbox)
    
    ax.text(5, 2.2, 'ONOMATOPOEIA PATTERN: "n-t-r" Resonance', 
            ha='center', va='center', fontsize=14, fontweight='bold', 
            color=COLORS['mythology'])
    
    ax.text(5, 1.8, 'NATRON → NEUTRON → NETER → NETHER', 
            ha='center', va='center', fontsize=12, 
            color='white', fontfamily='monospace')
    
    ax.text(5, 1.6, 'Sound of glassification events encoded in ancient languages', 
            ha='center', va='center', fontsize=10, 
            color='lightgray', style='italic')
    
    plt.tight_layout()
    plt.savefig('motif_overview.png', dpi=300, bbox_inches='tight', 
                facecolor='black', edgecolor='none')
    plt.close()
    
    print("✓ Created motif_overview.png")

def create_predictive_formulas():
    """Visualize the predictive mathematical formulas"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle('PREDICTIVE FORMULAS: Mathematical Archaeology Framework', 
                fontsize=20, fontweight='bold', color='white')
    
    # Formula Set A - Spatial Calculations
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.add_patch(Rectangle((1, 7), 8, 2, facecolor=COLORS['megalith'], alpha=0.3))
    ax1.text(5, 8.5, 'FORMULA SET A: Spatial Calculations', 
            ha='center', va='center', fontsize=14, fontweight='bold')
    ax1.text(5, 7.7, 'A1: Serpent Strike Distance\nA2: Vitrification Zone Radius\nA3: Lake Formation Probability', 
            ha='center', va='center', fontsize=10)
    
    # Formula Set B - Temporal Calculations  
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.add_patch(Rectangle((1, 7), 8, 2, facecolor=COLORS['energy'], alpha=0.3))
    ax2.text(5, 8.5, 'FORMULA SET B: Temporal Calculations', 
            ha='center', va='center', fontsize=14, fontweight='bold')
    ax2.text(5, 7.7, 'B1: Strike Timeline\nB2: Dragon Return Cycle\nB3: Energy Decay Rate', 
            ha='center', va='center', fontsize=10)
    
    # Formula Set C - Archaeological Predictions
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    ax3.axis('off')
    ax3.add_patch(Rectangle((1, 7), 8, 2, facecolor=COLORS['serpent'], alpha=0.3))
    ax3.text(5, 8.5, 'FORMULA SET C: Archaeological Predictions', 
            ha='center', va='center', fontsize=14, fontweight='bold')
    ax3.text(5, 7.7, 'C1: Vitrification Probability\nC2: Scar Preservation Index\nC3: Mythology Correlation', 
            ha='center', va='center', fontsize=10)
    
    # Example calculation visualization
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 10)
    ax4.axis('off')
    ax4.add_patch(Rectangle((1, 6), 8, 3, facecolor=COLORS['civilization'], alpha=0.3))
    ax4.text(5, 8.5, 'EXAMPLE: Wadi Natrun Analysis', 
            ha='center', va='center', fontsize=14, fontweight='bold')
    ax4.text(5, 7.5, 'Distance to nearest energy strike: 15.7 km\nVitrification probability: 0.73\nOnomatopoeia strength: 0.89', 
            ha='center', va='center', fontsize=11, fontfamily='monospace')
    
    # Add mathematical formulas as text boxes
    formula_examples = [
        "D = √[(x₂-x₁)² + (y₂-y₁)²] × φ",
        "R = (Energy_Level × Mass_Coeff) / π", 
        "P = (Tear_Volume × Serpent_Size) / Distance²"
    ]
    
    for i, formula in enumerate(formula_examples):
        ax4.text(5, 6.7 - i*0.3, formula, ha='center', va='center', 
                fontsize=10, fontfamily='monospace', color='yellow')
    
    plt.tight_layout()
    plt.savefig('predictive_formulas.png', dpi=300, bbox_inches='tight',
                facecolor='black', edgecolor='none')
    plt.close()
    
    print("✓ Created predictive_formulas.png")

def create_victoria_crash_diagram():
    """Visualize the proposed Victoria Lake crash site"""
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    
    # Create impact crater
    crater = Circle((0, 0), 1.5, facecolor='darkblue', alpha=0.7, edgecolor='red', linewidth=3)
    ax.add_patch(crater)
    
    # Central peak
    peak = Circle((0, 0), 0.3, facecolor='red', alpha=0.9)
    ax.add_patch(peak)
    
    # Energy rays
    angles = np.linspace(0, 2*np.pi, 12)
    for angle in angles:
        x_end = 1.8 * np.cos(angle)
        y_end = 1.8 * np.sin(angle)
        ax.plot([0, x_end], [0, y_end], 'yellow', linewidth=2, alpha=0.8)
    
    # Annotations
    ax.text(0, -1.8, 'Victoria Lake Crash Site', ha='center', va='center', 
           fontsize=16, fontweight='bold', color='white')
    ax.text(0, -1.95, 'Proposed Energy Weapon Impact Zone', ha='center', va='center', 
           fontsize=12, color='lightgray')
    
    # Add measurements
    ax.annotate('1.0°S, 33.0°E', xy=(1.5, 0), xytext=(1.8, 0.5),
               arrowprops=dict(arrowstyle='->', color='white', lw=2),
               fontsize=10, color='white', ha='center')
    
    ax.text(-1.8, 1.8, 'Exotic Isotopic\nSignatures Predicted', 
           ha='center', va='center', fontsize=10, color='yellow',
           bbox=dict(boxstyle='round', facecolor='black', alpha=0.7))
    
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('black')
    
    plt.tight_layout()
    plt.savefig('victoria_crash_diagram.png', dpi=300, bbox_inches='tight',
                facecolor='black', edgecolor='none')
    plt.close()
    
    print("✓ Created victoria_crash_diagram.png")

def create_onomatopoeia_network():
    """Create network diagram of onomatopoeia connections"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Create network graph
    G = nx.Graph()
    
    # Add nodes with onomatopoeia words
    words = ['NATRON', 'NEUTRON', 'NETER', 'MJÖLNIR', 'VAJRA', 'ANTIMONY', 'AETHER']
    positions = {
        'NATRON': (0, 2),
        'NEUTRON': (2, 2), 
        'NETER': (1, 0.5),
        'MJÖLNIR': (-2, 1.5),
        'VAJRA': (-2, 0.5),
        'ANTIMONY': (0, -1),
        'AETHER': (2, -0.5)
    }
    
    # Add edges showing connections
    connections = [
        ('NATRON', 'NEUTRON'),
        ('NATRON', 'NETER'),
        ('NEUTRON', 'AETHER'),
        ('MJÖLNIR', 'VAJRA'),
        ('ANTIMONY', 'AETHER')
    ]
    
    G.add_nodes_from(words)
    G.add_edges_from(connections)
    
    # Draw the network
    nx.draw_networkx_nodes(G, positions, node_color=COLORS['mythology'], 
                          node_size=2000, alpha=0.8, ax=ax)
    nx.draw_networkx_edges(G, positions, edge_color='white', 
                          width=2, alpha=0.6, ax=ax)
    nx.draw_networkx_labels(G, positions, font_size=12, font_weight='bold', 
                           font_color='white', ax=ax)
    
    # Add interpretation boxes
    ax.text(-2.5, -2, 'CRYSTAL/VITRIFICATION\nTERMS', ha='center', va='center', 
           fontsize=10, color=COLORS['energy'], fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='black', alpha=0.8))
    
    ax.text(2.5, -2, 'ENERGY STRIKE\nSOUNDS', ha='center', va='center', 
           fontsize=10, color=COLORS['serpent'], fontweight='bold',
           bbox=dict(boxstyle='round', facecolor='black', alpha=0.8))
    
    ax.text(0, 3, 'ONOMATOPOEIA NETWORK: "n-t-r" Resonance Pattern', 
           ha='center', va='center', fontsize=16, fontweight='bold', color='white')
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 4)
    ax.axis('off')
    ax.set_facecolor('black')
    
    plt.tight_layout()
    plt.savefig('onomatopoeia_network.png', dpi=300, bbox_inches='tight',
                facecolor='black', edgecolor='none')
    plt.close()
    
    print("✓ Created onomatopoeia_network.png")

def create_flood_timeline():
    """Create timeline of mythological flood events"""
    fig, ax = plt.subplots(figsize=(16, 8))
    
    # Timeline data
    events = [
        (-50000, 'Proto-Indo-European\nDragon Myths Begin', COLORS['mythology']),
        (-30000, 'Vedic Tradition\nIndra vs Vritra', COLORS['serpent']),
        (-15000, 'Norse Tradition\nThor vs Jormungand', COLORS['energy']),
        (-10000, 'Egyptian Tradition\nSet vs Apep', COLORS['megalith']),
        (-5000, 'Mesopotamian\n Marduk vs Tiamat', COLORS['civilization']),
        (-3000, 'Chinese Tradition\nYu the Great', COLORS['lake'])
    ]
    
    # Draw timeline
    ax.plot([-55000, 0], [0, 0], 'white', linewidth=4, alpha=0.8)
    
    # Add events
    for year, event, color in events:
        ax.plot([year, year], [-0.1, 0.1], 'white', linewidth=3)
        
        # Event box
        bbox = FancyBboxPatch((year-2000, 0.3), 4000, 1.5, 
                             boxstyle="round,pad=0.2", 
                             facecolor=color, alpha=0.3,
                             edgecolor=color, linewidth=2)
        ax.add_patch(bbox)
        
        ax.text(year, 1.05, event, ha='center', va='center', 
               fontsize=10, fontweight='bold', color='white')
        
        # Year label
        ax.text(year, -0.3, f'{abs(year):,} BCE', ha='center', va='center', 
               fontsize=9, color='lightgray')
    
    # Add pattern recognition box
    pattern_bbox = FancyBboxPatch((-50000, -2.5), 50000, 1, 
                                 boxstyle="round,pad=0.2", 
                                 facecolor=COLORS['mythology'], alpha=0.5,
                                 edgecolor=COLORS['mythology'], linewidth=3)
    ax.add_patch(pattern_bbox)
    
    ax.text(0, -2, 'GLOBAL PATTERN: Universal serpent/dragon mythology suggests\nshared cosmic events rather than cultural diffusion', 
           ha='center', va='center', fontsize=12, fontweight='bold', color='white')
    
    ax.set_xlim(-55000, 2000)
    ax.set_ylim(-3, 3)
    ax.set_xlabel('Timeline (Years BCE)', fontsize=12, color='white')
    ax.set_title('MYTHOLOGICAL FLOOD EVENTS: Global Pattern Timeline', 
                fontsize=16, fontweight='bold', color='white', pad=20)
    
    # Remove y-axis
    ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ax.tick_params(colors='white')
    ax.set_facecolor('black')
    
    plt.tight_layout()
    plt.savefig('flood_timeline.png', dpi=300, bbox_inches='tight',
                facecolor='black', edgecolor='none')
    plt.close()
    
    print("✓ Created flood_timeline.png")

def main():
    """Generate all visualizations"""
    print("🎨 Generating publication-quality visualizations...")
    print()
    
    # Create all visualizations
    create_motif_overview()
    create_predictive_formulas()
    create_victoria_crash_diagram()
    create_onomatopoeia_network()
    create_flood_timeline()
    
    print()
    print("✅ All visualizations generated successfully!")
    print("📊 Generated files:")
    print("   • motif_overview.png")
    print("   • predictive_formulas.png") 
    print("   • victoria_crash_diagram.png")
    print("   • onomatopoeia_network.png")
    print("   • flood_timeline.png")
    print()
    print("🚀 Ready for publication and presentation!")

if __name__ == "__main__":
    main()