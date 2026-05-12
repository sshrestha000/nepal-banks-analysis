import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"G:\DA\web_scraping\ClassA_Commercial_Banks.csv")

print("ORIGINAL DATA INFO")
df.info()
print('\nColumns:', df.columns.tolist())

# CLEAN CURRENCY COLUMNS

df["Paid-up capital"] = (
    df["Paid-up capital"]
    .str.replace("रु", '', regex=False)
    .str.replace("Arab", '', regex=False)
    .str.strip()
    .astype(float) * 1000000000
)

df["Total Assets"] = (
    df["Total Assets"]
    .str.replace("रु", '', regex=False)
    .str.replace("Arab", '', regex=False)
    .str.strip()
    .astype(float) * 1000000000
)

print("\n")
print("DATA TYPES AFTER CLEANING")
print("\n")
print(df.dtypes)

# SPLIT HEADQUARTERS INTO CITY AND DISTRICT
df[["City", "District"]] = df["Headquarters"].str.split(',', expand=True)
print("\n")
print("FIRST FEW ROWS")
print("\n")
print(df.head())

# REMOVE DUPLICATES
df = df.drop_duplicates()

# CALCULATE ADDITIONAL METRICS
df['assets_per_branch'] = df['Total Assets'] / df['Branches']
df['leverage_ratio'] = df['Total Assets'] / df['Paid-up capital']

# TOP 10 BANKS BY ASSETS - Pie Chart
top_banks = df.nlargest(10, "Total Assets")

plt.figure(figsize=(12, 10))
plt.pie(top_banks['Total Assets'], labels=top_banks['Bank Name'], 
        autopct='%1.1f%%', startangle=90)
plt.title("Top 10 Banks by Assets", fontsize=14, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.show()


# SCATTER PLOT: Branches vs Total Assets
plt.figure(figsize=(10, 6))
plt.scatter(df['Branches'], df['Total Assets'] / 1e9, 
            alpha=0.7, c='steelblue', edgecolors='white', s=100)
plt.xlabel('Number of Branches', fontsize=12)
plt.ylabel('Total Assets (Billions NPR)', fontsize=12)
plt.title('Branches vs Total Assets', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# BAR CHART: Assets per Branch
df_sorted = df.sort_values('assets_per_branch', ascending=True)

plt.figure(figsize=(12, 8))
plt.barh(df_sorted['Bank Name'], df_sorted['assets_per_branch'] / 1e9, 
         color='steelblue', edgecolor='white')
plt.xlabel('Assets per Branch (Billions NPR)', fontsize=12)
plt.title('Branch Efficiency: Assets per Branch', fontsize=14)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.show()

# HISTOGRAM: Distribution of Key Metrics
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Branches distribution
axes[0, 0].hist(df['Branches'], bins=15, color='steelblue', edgecolor='white')
axes[0, 0].set_xlabel('Number of Branches')
axes[0, 0].set_ylabel('Frequency')
axes[0, 0].set_title('Branch Distribution')

# Total Assets distribution
axes[0, 1].hist(df['Total Assets'] / 1e9, bins=15, color='coral', edgecolor='white')
axes[0, 1].set_xlabel('Total Assets (Billions NPR)')
axes[0, 1].set_ylabel('Frequency')
axes[0, 1].set_title('Assets Distribution')

# Assets per branch distribution
axes[1, 0].hist(df['assets_per_branch'] / 1e9, bins=15, color='green', edgecolor='white')
axes[1, 0].set_xlabel('Assets per Branch (Billions NPR)')
axes[1, 0].set_ylabel('Frequency')
axes[1, 0].set_title('Efficiency Distribution')

# Leverage ratio distribution
axes[1, 1].hist(df['leverage_ratio'], bins=15, color='purple', edgecolor='white')
axes[1, 1].set_xlabel('Leverage Ratio (Assets/Equity)')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].set_title('Leverage Distribution')

plt.suptitle('Banking Sector Distribution Analysis', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# SUMMARY STATISTICS
print("\n")
print("SUMMARY STATISTICS")
print("\n")
print(f"Total Banks: {len(df)}")
print(f"Total Branches: {df['Branches'].sum():,.0f}")
print(f"Total Assets: रु {df['Total Assets'].sum()/1e11:.2f} Arab")
print(f"Average Branches per Bank: {df['Branches'].mean():.0f}")
print(f"Average Assets per Branch: रु {df['assets_per_branch'].mean()/1e9:.2f} Billion")
print(f"Average Leverage Ratio: {df['leverage_ratio'].mean():.2f}x")

print("\n")
print("TOP 5 BANKS BY ASSETS")
print("\n")
top_assets = df.nlargest(5, 'Total Assets')[['Bank Name', 'Total Assets', 'Branches', 'leverage_ratio']]
for i, row in top_assets.iterrows():
    print(f"  {row['Bank Name']}: रु {row['Total Assets']/1e9:.0f}B assets, {row['Branches']:.0f} branches")
print("\n")
print("MOST EFFICIENT BANKS (Assets per Branch)")
top_efficient = df.nlargest(5, 'assets_per_branch')[['Bank Name', 'assets_per_branch', 'Branches']]
for i, row in top_efficient.iterrows():
    print(f"  {row['Bank Name']}: रु {row['assets_per_branch']/1e9:.1f}B per branch")

print("\n")
print("LEVERAGE ANALYSIS")
print(f"Highest Leverage: {df.loc[df['leverage_ratio'].idxmax(), 'Bank Name']} ({df['leverage_ratio'].max():.2f}x)")
print(f"Lowest Leverage: {df.loc[df['leverage_ratio'].idxmin(), 'Bank Name']} ({df['leverage_ratio'].min():.2f}x)")