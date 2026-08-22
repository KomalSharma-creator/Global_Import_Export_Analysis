import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from pathlib import Path
st.set_page_config(
    page_title='World Import & Export Trade Project',
    page_icon='🚢',
    layout='wide',
    initial_sidebar_state='expanded'
)
css = Path(r"C:\python DS10-12\komal\styling.css").read_text(encoding='utf-8')
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
df = pd.read_csv('Cleaned_dataset1.csv')
df1 = pd.read_csv('Cleaned_dataset2.csv')
merged = pd.merge(
    df,
    df1,
    on=["Country", "Year"],
    how="left")
def chart_title(title, icon="📊"):
    st.markdown(
        f"""
        <h3 class="chart-title">{icon} {title}</h3>
        """,
        unsafe_allow_html=True,)
def styled_chart(fig, height=450):
    fig.update_layout(
        title_text="",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(
            family="Inter, sans-serif",
            size=13,
            color="#F8FAFC"
        ),
        legend=dict(
            bgcolor="rgba(15, 23, 42, 0.8)",
            bordercolor="#38BDF8",
            borderwidth=1,
            font=dict(size=12, color="#F8FAFC")
        ),
        hoverlabel=dict(
            bgcolor="#08111F",
            bordercolor="#38BDF8",
            font_size=13,
            font_color="white"
        ),
        transition=dict(duration=350),
        margin=dict(l=60, r=25, t=25, b=55),
        height=height,
    )
    fig.update_xaxes(
        title_font=dict(size=15, color="#F8FAFC"),
        tickfont=dict(size=12, color="#A7F3D0"),
        showgrid=False,
        showline=True,
        linecolor="#38BDF8",
        linewidth=2
    )
    fig.update_yaxes(
        title_font=dict(size=15, color="#F8FAFC"),
        tickfont=dict(size=12, color="#A7F3D0"),
        showgrid=True,
        gridcolor="rgba(56, 189, 248, 0.15)",
        showline=True,
        linecolor="#38BDF8",
        linewidth=2,
        zeroline=False
    )
    for trace in fig.data:
        if trace.type == "scatter":
            trace.update(
                line=dict(width=3),
                marker=dict(size=7, line=dict(color="white", width=1))
            )
        elif trace.type == "bar":
            trace.update(
                marker_line_width=1.5,
                marker_line_color="#ECFDF5"
            )
        elif trace.type == "pie":
            trace.update(
                textfont_size=13,
                pull=[0.02] * len(trace.labels) if hasattr(trace, 'labels') and trace.labels is not None else None
            )
    return fig
def show_chart(fig, title=None, icon="📊", height=450):
    fig = styled_chart(fig, height)
    if title:
        chart_title(title, icon)
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displaylogo": False,
            "displayModeBar": False,
            "responsive": True,},)
with st.sidebar:
    st.markdown("""
        <div style="text-align:center; padding:12px 0 18px 0;">
        <h2 style="
                color:#F8FAFC;
                margin:0;
                font-size:2.02rem;
                font-weight:700;
            ">
                🚢 Global Trade
            </h2>
        <p style="
                color:#A7F3D0;
                font-size:0.82rem;
                letter-spacing:2px;
                font-weight:700;
                margin-top:6px;
            ">
                INTELLIGENCE PLATFORM 
                DEVELOPED BY KOMAL SHARMA
            </p>
        </div>
    """, unsafe_allow_html=True)
    pages = {
        "🏠 Home": "home",
        "📥 Import Analytics": "import",
        "📤 Export Analytics": "export",
        "📈 Trade Comparison": "comparison",
        "🛃 Tariff Analysis": "tariff",
        "🌍 Geographic Analysis": "geo",
        "📊 Growth & Competitiveness": "growth",
        "📙 Dataset": "dataset",
        "⚙️ Pre Processing": "preprocessing",
        "👤 About": "about",
        "🤖 ChatBot": "chatbot",
    }
    page = st.radio(
        "",
        list(pages.keys()),
        label_visibility="collapsed")
    st.divider()
    st.markdown(
        "<p style='color:#A7F3D0;font-size:.78rem;font-weight:700;'>FILTER CONTROLS</p>",
        unsafe_allow_html=True)
    year = st.multiselect(
        "📅 Select Year",
        sorted(merged["Year"].dropna().unique()))
    continent = st.multiselect(
        "🌍 Select Continent",
        sorted(merged["Continent"].dropna().unique()))
    income = st.multiselect(
        "💰 Income Group",
        sorted(merged["Income_Group"].dropna().unique()))
    if continent:
        country_options = sorted(
            merged[
                merged["Continent"].isin(continent)
            ]["Country"]
            .dropna()
            .unique())
    else:
        country_options = sorted(
            merged["Country"]
            .dropna()
            .unique())
    country = st.multiselect(
        "🏳️ Select Country",
        country_options)
    st.divider()
    filtered = merged.copy()
    if year:
        filtered = filtered[
            filtered["Year"].isin(year)]
    if income:
        filtered = filtered[
            filtered["Income_Group"].isin(income)]
    if continent:
        filtered = filtered[
            filtered["Continent"].isin(continent)]
    if country:
        filtered = filtered[
            filtered["Country"].isin(country)]
if page == '🏠 Home':
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">🌍 Global Trade Intelligence Platform</div>
        <div class="hero-subtitle">Executive Analytics for World Imports, Exports & Macroeconomic Indicators</div>
        <div class="hero-tags">
            <span class="tag">1990 – 2023 Coverage</span>
            <span class="tag">190+ Global Markets</span>
            <span class="tag">World Bank & WTO Metrics</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<h3 class='section-header'>📊 Executive Summary</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="summary-box">
        This platform delivers real-time macroeconomic trade analytics, highlighting cross-border commodity flows, 
        tariff structures, regional balances, and global competitiveness metrics. Use the dynamic sidebar parameters 
        to isolate multi-year historical trends across regional economic blocs.
    </div>
    """, unsafe_allow_html=True)
    countries_count = filtered["Country"].nunique()
    years_count = filtered["Year"].nunique()
    imports = filtered["Import_Value"].sum()
    exports = filtered["Export_Value"].sum()
    trade_volume = imports + exports
    trade_balance = exports - imports
    world_growth = filtered["World Growth (%)"].mean()
    mfn = filtered["MFN Simple Average (%)"].mean()
    st.markdown("<h3 class='section-header'>📌 Macroeconomic Overview</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
            <div class="kpi-label">🌍 Active Economies</div>
            <div class="kpi-value">{countries_count:,}</div>
            <div class="kpi-sub">Total tracked markets</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
            <div class="kpi-label">⏳ Time Horizon</div>
            <div class="kpi-value">{years_count:,} <span style="font-size:1rem; font-weight:400; color:#64748B;">Years</span></div>
            <div class="kpi-sub">Historical coverage</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="kpi-card accent-emerald">
            <div class="kpi-label">📥 Total Import Value</div>
            <div class="kpi-value">${imports/1e12:.2f} T</div>
            <div class="kpi-sub">Gross imports sum</div>
        </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown(f"""
        <div class="kpi-card accent-emerald">
            <div class="kpi-label">📤 Total Export Value</div>
            <div class="kpi-value">${exports/1e12:.2f} T</div>
            <div class="kpi-sub">Gross exports sum</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("<div style='margin-bottom: 12px;'></div>", unsafe_allow_html=True)
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.markdown(f"""
        <div class="kpi-card accent-purple">
            <div class="kpi-label">💹 Total Trade Volume</div>
            <div class="kpi-value">${trade_volume/1e12:.2f} T</div>
            <div class="kpi-sub">Imports + Exports sum</div>
        </div>
        """, unsafe_allow_html=True)
    with col6:
        balance_class = "accent-emerald" if trade_balance >= 0 else "accent-red"
        st.markdown(f"""
        <div class="kpi-card {balance_class}">
            <div class="kpi-label">⚖️ Net Trade Balance</div>
            <div class="kpi-value">${trade_balance/1e12:.2f} T</div>
            <div class="kpi-sub">Exports minus Imports</div>
        </div>
        """, unsafe_allow_html=True)
    with col7:
        st.markdown(f"""
        <div class="kpi-card accent-gold">
            <div class="kpi-label">📈 Avg World Growth</div>
            <div class="kpi-value">{world_growth:.2f}%</div>
            <div class="kpi-sub">Annual expansion rate</div>
        </div>
        """, unsafe_allow_html=True)
    with col8:
        st.markdown(f"""
        <div class="kpi-card accent-slate">
            <div class="kpi-label">🛃 Avg MFN Tariff Rate</div>
            <div class="kpi-value">{mfn:.2f}%</div>
            <div class="kpi-sub">Simple average tariff</div>
        </div>
        """, unsafe_allow_html=True)
        top10 = (
            filtered.groupby(["Year", "Country"])["Export_Value"]
            .sum()
            .reset_index()
        )
        top_countries = (
            top10.groupby("Country")["Export_Value"]
            .sum()
            .nlargest(10)
            .index
        )
        top10 = top10[top10["Country"].isin(top_countries)]
        fig = px.line(
        top10,
        x="Year",
        y="Export_Value",
        color="Country",
        markers=True,
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    show_chart(
        fig,
        title="Export Performance Over Time (Top 10 Economies)",
        icon="🚢"
    )
    continent_df = filtered.groupby("Continent").size().reset_index(name="Countries")
    fig = px.pie(
        continent_df,
        names="Continent",
        values="Countries",
        hole=0.5,
        color_discrete_sequence=px.colors.qualitative.Safe
    )
    show_chart(
        fig,
        title="Distribution of Covered Economies by Geographic Area",
        icon="🌍",
        height=420
    )
    st.markdown("""
        <div class="dashboard-footer">
            © 2026 Global Trade Intelligence Platform • Financial Analytics Division
        </div>
    """, unsafe_allow_html=True)
elif page == "📥 Import Analytics":
    st.title("📥 Import Analytics")
    total_import = filtered["Import_Value"].sum()
    avg_import = filtered["Import_Value"].mean()
    countries = filtered["Country"].nunique()
    latest_year = filtered["Year"].max()
    previous_year = latest_year - 1
    latest_import = filtered.loc[
        filtered["Year"] == latest_year,
        "Import_Value"
    ].sum()
    previous_import = filtered.loc[
        filtered["Year"] == previous_year,
        "Import_Value"
    ].sum()
    growth = 0
    if previous_import != 0:
        growth = ((latest_import - previous_import) /
                previous_import) * 100
    st.subheader("📌 Import Overview")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">📥 Total Imports</div>
                <div class="kpi-value">${total_import/1e12:.2f} T</div>
            </div>
            """,
            unsafe_allow_html=True)
    with col2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">📊 Average Imports</div>
                <div class="kpi-value">${avg_import/1e9:.2f} B</div>
            </div>
            """,
            unsafe_allow_html=True)
    with col3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">🌍 Countries</div>
                <div class="kpi-value">{countries}</div>
            </div>
            """,
            unsafe_allow_html=True)
    with col4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-title">📈 Growth</div>
                <div class="kpi-value">{growth:.2f}%</div>
            </div>
            """,
            unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📈 Overall Import Growth Trend")
        import_trend = (
            filtered.groupby("Year")["Import_Value"]
            .sum()
            .reset_index()
        )
        fig = px.line(
            import_trend,
            x="Year",
            y="Import_Value",
            markers=True,
            title="Global Import Growth Over Years",
            color_discrete_sequence=["#91F37B"]
        )
        fig.update_traces(
            line=dict(width=3),
            hovertemplate="<b>Year %{x}</b><br>Import Value: %{y:,.0f}"
        )
        fig.update_layout(
            plot_bgcolor="#1E1E2F",
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#FF6F61")
        )
        show_chart(fig, height=500)
    with col2:
        st.subheader("🌍 Top 10 Import Countries")
        top_countries = (
            filtered.groupby("Country")["Import_Value"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )
        fig = px.bar(
            top_countries,
            x="Import_Value",
            y="Country",
            orientation="h",
            title="Top 10 Countries by Import Value",
            color="Import_Value",
            color_continuous_scale="Plasma"
        )
        fig.update_traces(
            hovertemplate="<b>%{y}</b><br>Import Value: %{x:,.0f}"
        )
        fig.update_layout(
            plot_bgcolor="#1E1E2F",
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#FFD700"),
            coloraxis_colorbar=dict(title="Import Value", tickformat=".2s")
        )
        show_chart(fig, height=500)
    with col1:
        st.subheader("🌐 Global Import Distribution Map")
        country_import_map = (
            filtered.groupby("Country")["Import_Value"]
            .sum()
            .reset_index()
        )
        fig = px.choropleth(
            country_import_map,
            locations="Country",
            locationmode="country names",
            color="Import_Value",
            hover_name="Country",
            color_continuous_scale="Turbo",
            title="Global Import Value by Country"
        )
        fig.update_layout(
            height=550,
            geo=dict(showframe=False, showcoastlines=True, bgcolor="#121212"),
            coloraxis_colorbar_title="Import Value",
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#00CED1")
        )
        show_chart(fig, height=550)
    with col2:
        st.subheader("🌎 Imports by Continent")
        continent_import = (
            filtered.groupby("Continent")["Import_Value"]
            .sum()
            .reset_index()
            .sort_values("Import_Value", ascending=False)
        )
        fig = px.bar(
            continent_import,
            x="Continent",
            y="Import_Value",
            title="Total Imports by Continent",
            color="Continent",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig.update_traces(
            hovertemplate="<b>%{x}</b><br>Import Value: %{y:,.0f}"
        )
        fig.update_layout(
            plot_bgcolor="#1E1E2F",
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#32CD32")
        )
        show_chart(fig, height=450)
    with col1:
        st.subheader("📊 Imports by Income Group")
        income_import = (
            filtered.groupby("Income_Group")["Import_Value"]
            .sum()
            .reset_index()
            .sort_values("Import_Value", ascending=False)
        )
        fig = px.bar(
            income_import,
            x="Income_Group",
            y="Import_Value",
            title="Total Imports by Income Group",
            color="Income_Group",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig.update_traces(
            hovertemplate="<b>%{x}</b><br>Import Value: %{y:,.0f}"
        )
        fig.update_layout(
            plot_bgcolor="#1E1E2F",
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#FF69B4")
        )
        show_chart(fig, height=450)
    with col2:
        st.subheader("🌳 Import Contribution by Country")
        treemap_data = (
            filtered.groupby("Country")["Import_Value"]
            .sum()
            .reset_index()
            .sort_values("Import_Value", ascending=False)
        )
        fig = px.treemap(
            treemap_data,
            path=["Country"],
            values="Import_Value",
            title="Country-wise Import Contribution",
            color="Import_Value",
            color_continuous_scale="Viridis"
        )
        fig.update_traces(
            hovertemplate="<b>%{label}</b><br>Import Value: %{value:,.0f}"
        )
        fig.update_layout(
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#FFA500")
        )
        show_chart(fig, height=600)
    st.subheader("🧠 Key Import Insights")
    highest_country = (filtered.groupby("Country")["Import_Value"]
        .sum()
        .idxmax())
    highest_country_value = (filtered.groupby("Country")["Import_Value"]
        .sum()
        .max())
    highest_year = (filtered.groupby("Year")["Import_Value"]
        .sum()
        .idxmax())
    highest_continent = ( filtered.groupby("Continent")["Import_Value"]
        .sum()
        .idxmax())
    col1, col2, col3 = st.columns(3)
    with col1:
            st.markdown(f"""
            <div class="analytics-card">
                <div class="analytics-icon">🌍</div>
                <div class="analytics-title">Top Import Country</div>
                <div class="analytics-value">{highest_country}</div>
                <div class="analytics-sub">
                    Import Value: <b>${highest_country_value/1e9:.2f} B</b>
                </div>
            </div>
            """, unsafe_allow_html=True)
    with col2:
            st.markdown(f"""
            <div class="analytics-card">
                <div class="analytics-icon">📅</div>
                <div class="analytics-title">Peak Import Year</div>
                <div class="analytics-value">{highest_year}</div>
                <div class="analytics-sub">
                    Highest global import activity recorded.
                </div>
            </div>
            """, unsafe_allow_html=True)
    with col3:
            st.markdown(f"""
            <div class="analytics-card">
                <div class="analytics-icon">🌎</div>
                <div class="analytics-title">Leading Continent</div>
                <div class="analytics-value">{highest_continent}</div>
                <div class="analytics-sub">
                    Highest total import contribution.
                </div>
            </div>
            """, unsafe_allow_html=True)
elif page == "📤 Export Analytics":
    st.title("📤 Export Analytics")
    st.markdown(
        "<h4 style='color:#FFFFFF;'>Global Export Performance Analysis</h4>",
        unsafe_allow_html=True)
    total_export = filtered["Export_Value"].sum()
    avg_export = filtered["Export_Value"].mean()
    countries = filtered["Country"].nunique()
    latest_year = filtered["Year"].max()
    previous_year = latest_year - 1
    latest_export = filtered.loc[
        filtered["Year"] == latest_year,
        "Export_Value"
    ].sum()
    previous_export = filtered.loc[
        filtered["Year"] == previous_year,
        "Export_Value"
    ].sum()
    growth = 0
    if previous_export != 0:
        growth = ((latest_export - previous_export) /
                  previous_export) * 100
    st.subheader("📊 Export Overview")
    c1,c2,c3,c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="export-card">
        <div class="export-title">
        📤 Total Exports
        </div>
        <div class="export-value">
        ${total_export/1e12:.2f} T
        </div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="export-card">
        <div class="export-title">
        📈 Average Export
        </div>
        <div class="export-value">
        ${avg_export/1e9:.2f} B
        </div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="export-card">
        <div class="export-title">
        🌍 Export Countries
        </div>
        <div class="export-value">
        {countries}
        </div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="export-card">
        <div class="export-title">
        🚀 Export Growth
        </div>
        <div class="export-value">
        {growth:.2f}%
        </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("📈 Global Export Trend")
    export_trend = (
        filtered.groupby("Year")["Export_Value"]
        .sum()
        .reset_index()
    )
    fig = px.line(
        export_trend,
        x="Year",
        y="Export_Value",
        markers=True,
        line_shape="spline",
        title="Global Export Growth Over Years",
        color_discrete_sequence=["#64C782"]  # coral red line
    )
    fig.update_traces(
        hovertemplate="<b>Year %{x}</b><br>Export Value: %{y:,.0f}"
    )
    fig.update_layout(
        plot_bgcolor="#1E1E2F",
        paper_bgcolor="#121212",
        font=dict(color="white"),
        title_font=dict(size=20, color="#FF6F61")
    )
    show_chart(fig)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏆 Top 10 Export Countries")
        top_export = (
            filtered.groupby("Country")["Export_Value"]
            .sum()
            .sort_values(ascending=False)
            .nlargest(10)
            .reset_index()
        )
        fig = px.bar(
            top_export,
            x="Export_Value",
            y="Country",
            orientation="h",
            color="Export_Value",
            color_continuous_scale="Sunset"
        )
        fig.update_traces(
            hovertemplate="<b>%{y}</b><br>Export Value: %{x:,.0f>"
        )
        fig.update_layout(
            plot_bgcolor="#1E1E2F",
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#30C4FF"),
            height=500,
            yaxis={"categoryorder": "total ascending"},
            coloraxis_colorbar=dict(title="Export Value", tickformat=".2s")
        )
        show_chart(fig)
    with col2:
        st.subheader("🌎 Export Share by Continent")
        continent_export = (
            filtered.groupby("Continent")["Export_Value"]
            .sum()
            .reset_index()
        )
        fig = px.pie(
            continent_export,
            names="Continent",
            values="Export_Value",
            hole=0.55,
            color_discrete_sequence=px.colors.sequential.Viridis
        )
        fig.update_traces(
            hovertemplate="<b>%{label}</b><br>Export Value: %{value:,.0f}"
        )
        fig.update_layout(
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#32CD32")
        )
        show_chart(fig)
    with col1:
        st.subheader("🌍 Global Export Distribution")
        country_export = (
            filtered.groupby("Country")["Export_Value"]
            .sum()
            .reset_index()
        )
        fig = px.choropleth(
            country_export,
            locations="Country",
            locationmode="country names",
            color="Export_Value",
            hover_name="Country",
            color_continuous_scale="Magma",
            title="Global Export Value by Country"
        )
        fig.update_layout(
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#082112")
        )
        show_chart(fig)
    with col2:
        st.subheader("📊 Exports by Income Group")
        income_export = (
            filtered.groupby("Income_Group")["Export_Value"]
            .sum()
            .reset_index()
            .sort_values("Export_Value", ascending=False)
        )
        fig = px.bar(
            income_export,
            x="Income_Group",
            y="Export_Value",
            color="Export_Value",
            color_continuous_scale="Rainbow"
        )
        fig.update_traces(
            hovertemplate="<b>%{x}</b><br>Export Value: %{y:,.0f}"
        )
        fig.update_layout(
            plot_bgcolor="#1E1E2F",
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#00CED1"),
            height=500,
            xaxis_title="Income Group",
            yaxis_title="Export Value",
            coloraxis_colorbar=dict(title="Export Value", tickformat=".2s")
        )
        show_chart(fig)
    with col1:
        st.subheader("🌳 Country-wise Export Contribution")
        treemap_data = (
            filtered.groupby("Country")["Export_Value"]
            .sum()
            .reset_index()
            .sort_values("Export_Value", ascending=False)
        )
        fig = px.treemap(
            treemap_data,
            path=["Country"],
            values="Export_Value",
            color="Export_Value",
            color_continuous_scale="Viridis",
            title="Export Contribution"
        )
        fig.update_traces(
            hovertemplate="<b>%{label}</b><br>Export Value: %{value:,.0f}"
        )
        fig.update_layout(
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#FFA500")
        )
        show_chart(fig)
    with col2:
        st.subheader("☀️ Export Hierarchy")
        sunburst_data = (
            filtered.groupby(["Continent", "Country"])["Export_Value"]
            .sum()
            .reset_index()
        )
        fig = px.sunburst(
            sunburst_data,
            path=["Continent", "Country"],
            values="Export_Value",
            color="Export_Value",
            color_continuous_scale="Turbo"
        )
        fig.update_traces(
            hovertemplate="<b>%{label}</b><br>Export Value: %{value:,.0f}"
        )
        fig.update_layout(
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title_font=dict(size=20, color="#00BFFF")
        )
        show_chart(fig)
    with col1:
        st.subheader("📉 Export Value Distribution")
        fig = px.histogram(
            filtered,
            x="Export_Value",
            nbins=35,
            color_discrete_sequence=["#062A26"]
        )
        fig.update_traces(
            hovertemplate="Export Value: %{x:,.0f}<br>Frequency: %{y}"
        )
        fig.update_layout(
            plot_bgcolor="#1E1E2F",
            paper_bgcolor="#121212",
            font=dict(color="white"),
            title="Distribution of Export Values",
            title_font=dict(size=20, color="#FF6F61"),
            xaxis_title="Export Value",
            yaxis_title="Frequency",
            height=450
        )
        show_chart(fig)
    with col2:
        st.subheader("🔵 Import vs Export")
        fig = px.scatter(
            filtered,
            x="Import_Value",
            y="Export_Value",
            color="Continent",
            size="Export_Value",
            hover_name="Country",
            hover_data=["Year"],
            opacity=0.75,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(
            hovertemplate="<b>%{hovertext}</b><br>Year: %{customdata[0]}<br>Import: %{x:,.0f}<br>Export: %{y:,.0f}"
        )
        fig.update_layout(
            paper_bgcolor="#121212",
            plot_bgcolor="#1E1E2F",
            font=dict(color="white"),
            title_font=dict(size=20, color="#32CD32")
        )
        show_chart(fig)
    st.markdown("---")
    st.subheader("💡 Key Export Insights")
    highest_country = (
        filtered.groupby("Country")["Export_Value"]
        .sum()
        .idxmax())
    highest_country_value = (
        filtered.groupby("Country")["Export_Value"]
        .sum()
        .max())
    highest_year = (
        filtered.groupby("Year")["Export_Value"]
        .sum()
        .idxmax())
    highest_year_value = (
        filtered.groupby("Year")["Export_Value"]
        .sum()
        .max())
    highest_continent = (
        filtered.groupby("Continent")["Export_Value"]
        .sum()
        .idxmax())
    avg_export_country = (
        filtered.groupby("Country")["Export_Value"]
        .sum()
        .mean())
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="insight-card">
        <div class="insight-title">
        🏆 Top Export Country
        </div>
        <div class="insight-value">
        {highest_country}
        </div>
        <div class="insight-text">
        ${highest_country_value/1e12:.2f} Trillion
        </div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="insight-card">
        <div class="insight-title">
        📅 Peak Export Year
        </div>
        <div class="insight-value">
        {highest_year}
        </div>
        <div class="insight-text">
        ${highest_year_value/1e12:.2f} Trillion
        </div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="insight-card">
        <div class="insight-title">
        🌎 Leading Continent
        </div>
        <div class="insight-value">
        {highest_continent}
        </div>
        <div class="insight-text">
        Avg Export/Country:
        ${avg_export_country/1e9:.2f} Billion
        </div>
        </div>
        """, unsafe_allow_html=True)
elif page == "📈 Trade Comparison":
    st.title("📈 Trade Comparison")
    st.markdown(
        "<h4 style='section-header'>Compare Global Import & Export Performance</h4>",
        unsafe_allow_html=True)
    total_import = filtered["Import_Value"].sum()
    total_export = filtered["Export_Value"].sum()
    trade_volume = total_import + total_export
    trade_balance = total_export - total_import
    countries = filtered["Country"].nunique()
    st.subheader("📊 Trade Overview")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
            <div class="kpi-label">📥 Total Imports</div>
            <div class="kpi-value">${total_import/1e12:.2f} T</div>
            <div class="kpi-sub">Global Imports</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="kpi-card accent-emerald">
            <div class="kpi-label">📤 Total Exports</div>
            <div class="kpi-value">${total_export/1e12:.2f} T</div>
            <div class="kpi-sub">Global Exports</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="kpi-card accent-gold">
            <div class="kpi-label">💹 Trade Volume</div>
            <div class="kpi-value">${trade_volume/1e12:.2f} T</div>
            <div class="kpi-sub">Imports + Exports</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        color = "#00C853" if trade_balance >= 0 else "#FF3D00"
        st.markdown(f"""
        <div class="kpi-card accent-red">
            <div class="kpi-label">⚖ Trade Balance</div>
            <div class="kpi-value" style="color:{color};">${trade_balance/1e12:.2f} T</div>
            <div class="kpi-sub">Exports − Imports</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("📈 Import vs Export Trend")
    trade_trend = (
        filtered.groupby("Year")[["Import_Value","Export_Value"]]
        .sum()
        .reset_index())
    fig = px.line(
        trade_trend,
        x="Year",
        y=["Import_Value","Export_Value"],
        markers=True,
        color_discrete_sequence=["#1362EB","#00B4D8"])
    show_chart(fig)
    st.subheader("🏆 Top 10 Trading Countries")
    trade_country = (
        filtered.groupby("Country")[["Import_Value","Export_Value"]]
        .sum()
        .reset_index())
    trade_country["Trade_Volume"] = (
        trade_country["Import_Value"] +
        trade_country["Export_Value"])
    trade_country = (
        trade_country.sort_values(
            "Trade_Volume",
            ascending=False)
        .head(10))
    chart = trade_country.melt(
        id_vars="Country",
        value_vars=["Import_Value","Export_Value"],
        var_name="Trade Type",
        value_name="Trade Value")
    fig = px.bar(
        chart,
        x="Country",
        y="Trade Value",
        color="Trade Type",
        barmode="group",
        text="Trade Value",
        color_discrete_map={
            "Import_Value":"#1362EB",
            "Export_Value":"#00B4D8"})
    fig.update_layout(
        height=550,
        title="Top 10 Trading Countries",
        title_x=0.32,
        xaxis_title="Country",
        yaxis_title="Trade Value (USD)")
    fig.update_traces(
        texttemplate="$%{text:.2s}",
        textposition="outside")
    show_chart(fig)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌍 Trade Balance by Continent")
        continent_trade = (
            filtered.groupby("Continent")[["Import_Value", "Export_Value"]]
            .sum()
            .reset_index())
        continent_trade["Trade_Balance"] = (
            continent_trade["Export_Value"] -
            continent_trade["Import_Value"])
        fig = px.bar(
            continent_trade,
            x="Continent",
            y="Trade_Balance",
            color="Trade_Balance",
            text="Trade_Balance",
            color_continuous_scale="RdYlGn")
        fig.update_layout(
            template="plotly_white",
            height=500,
            title="Trade Balance by Continent",
            title_x=0.28,
            coloraxis_showscale=False,
            xaxis_title="Continent",
            yaxis_title="Trade Balance (USD)")
        fig.update_traces(
            texttemplate="$%{text:.2s}",
            textposition="outside")
        show_chart(fig)
    with col2:
        st.subheader("🌎 Trade Volume by Continent")
        continent_volume = (
            filtered.groupby("Continent")[["Import_Value", "Export_Value"]]
            .sum()
            .reset_index())
        continent_volume["Trade_Volume"] = (
            continent_volume["Import_Value"] +
            continent_volume["Export_Value"])
        fig = px.pie(
            continent_volume,
            names="Continent",
            values="Trade_Volume",
            hole=0.55,
            color_discrete_sequence=px.colors.sequential.Blues_r)
        show_chart(fig)
    st.markdown("---")
    st.subheader("🗺️ Global Trade Volume")
    world_trade = (
        filtered.groupby("Country")[["Import_Value", "Export_Value"]]
        .sum()
        .reset_index())
    world_trade["Trade_Volume"] = (
        world_trade["Import_Value"] +
        world_trade["Export_Value"])
    fig = px.choropleth(
        world_trade,
        locations="Country",
        locationmode="country names",
        color="Trade_Volume",
        hover_name="Country",
        color_continuous_scale="Viridis",
        title="Global Trade Volume")
    show_chart(fig)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌳 Trade Volume by Country")
        tree = world_trade.sort_values(
            "Trade_Volume",
            ascending=False)
        fig = px.treemap(
            tree,
            path=["Country"],
            values="Trade_Volume",
            color="Trade_Volume",
            color_continuous_scale="Blues")
        show_chart(fig)
    with col2:
        st.subheader("☀️ Trade Hierarchy")
        sunburst = (
            filtered.groupby(
                ["Continent", "Country"]
            )[["Import_Value", "Export_Value"]]
            .sum()
            .reset_index()
        )
        sunburst["Trade_Volume"] = (
            sunburst["Import_Value"] +
            sunburst["Export_Value"]
        )
        fig = px.sunburst(
            sunburst,
            path=["Continent", "Country"],
            values="Trade_Volume",
            color="Trade_Volume",
            color_continuous_scale="Blues"
        )
        show_chart(fig)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔵 Import vs Export Analysis")
        scatter = (
            filtered.groupby(["Country", "Continent"])[["Import_Value", "Export_Value"]]
            .sum()
            .reset_index()
        )
        scatter["Trade_Volume"] = (
            scatter["Import_Value"] +
            scatter["Export_Value"]
        )
        fig = px.scatter(
            scatter,
            x="Import_Value",
            y="Export_Value",
            color="Continent",
            size="Trade_Volume",
            hover_name="Country",
            size_max=40
        )
        fig.update_layout(
            template="plotly_white",
            height=500,
            title="Import vs Export Relationship",
            title_x=0.28,
            xaxis_title="Import Value",
            yaxis_title="Export Value"
        )
        show_chart(fig)
    with col2:
        st.subheader("🔥 Correlation Heatmap")
        corr = filtered[[
            "Import_Value",
            "Export_Value",
            "Country Growth (%)",
            "World Growth (%)",
            "MFN Simple Average (%)"
        ]].corr(numeric_only=True)
        fig = px.imshow(
            corr,
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            aspect="auto"
        )
        show_chart(fig)
    st.markdown("---")
    st.subheader("💡 Trade Insights")
    trade_country = (
        filtered.groupby("Country")[["Import_Value", "Export_Value"]]
        .sum()
    )
    trade_country["Trade_Volume"] = (
        trade_country["Import_Value"] +
        trade_country["Export_Value"]
    )
    best_country = trade_country["Trade_Volume"].idxmax()
    best_country_value = trade_country["Trade_Volume"].max()
    trade_year = (
        filtered.groupby("Year")[["Import_Value", "Export_Value"]]
        .sum()
    )
    trade_year["Trade_Volume"] = (
        trade_year["Import_Value"] +
        trade_year["Export_Value"]
    )
    best_year = trade_year["Trade_Volume"].idxmax()
    continent_trade = (
        filtered.groupby("Continent")[["Import_Value", "Export_Value"]]
        .sum()
    )
    continent_trade["Trade_Volume"] = (
        continent_trade["Import_Value"] +
        continent_trade["Export_Value"]
    )
    best_continent = continent_trade["Trade_Volume"].idxmax()
    a, b, c = st.columns(3)
    with a:
        st.markdown(f"""
        <div class="trade-insight">
        <div class="trade-head">
        🏆 Largest Trading Country
        </div>
        <div class="trade-body">
        {best_country}
        </div>
        <div class="trade-small">
        ${best_country_value/1e12:.2f} Trillion
        </div>
        </div>
        """, unsafe_allow_html=True)
    with b:
        st.markdown(f"""
        <div class="trade-insight">
        <div class="trade-head">
        📅 Peak Trade Year
        </div>
        <div class="trade-body">
        {best_year}
        </div>
        <div class="trade-small">
        Highest Global Trade Volume
        </div>
        </div>
        """, unsafe_allow_html=True)
    with c:
        st.markdown(f"""
        <div class="trade-insight">
        <div class="trade-head">
        🌍 Leading Trade Continent
        </div>
        <div class="trade-body">
        {best_continent}
        </div>
        <div class="trade-small">
        Highest Combined Trade
        </div>
        </div>
        """, unsafe_allow_html=True)
elif page == "🛃 Tariff Analysis":
    st.title("🛃 Tariff Analysis")
    st.markdown(
            "<h4 style='section-header'>Global Tariff Policy Analysis</h4>",
            unsafe_allow_html=True
        )
    avg_mfn = filtered["MFN Simple Average (%)"].mean()
    avg_ahs = filtered["AHS Simple Average (%)"].mean()
    highest_mfn = filtered["MFN Simple Average (%)"].max()
    lowest_mfn = filtered["MFN Simple Average (%)"].min()
    st.subheader("📊 Tariff Overview")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
            <div class="kpi-label">🛃 Avg MFN Tariff</div>
            <div class="kpi-value">{avg_mfn:.2f}%</div>
            <div class="kpi-sub">Mean across countries</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="kpi-card accent-emerald">
            <div class="kpi-label">🌍 Avg AHS Tariff</div>
            <div class="kpi-value">{avg_ahs:.2f}%</div>
            <div class="kpi-sub">Mean across countries</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="kpi-card accent-gold">
            <div class="kpi-label">📈 Highest MFN</div>
            <div class="kpi-value">{highest_mfn:.2f}%</div>
            <div class="kpi-sub">Top tariff rate</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="kpi-card accent-red">
            <div class="kpi-label">📉 Lowest MFN</div>
            <div class="kpi-value">{lowest_mfn:.2f}%</div>
            <div class="kpi-sub">Lowest tariff rate</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("📈 MFN Tariff Distribution")
    fig = px.histogram(
        filtered,
        x="MFN Simple Average (%)",
        nbins=35,
        color_discrete_sequence=["#69B9CB"]  # bright orange
    )
    fig.update_layout(
        template="plotly_white",
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        height=500,
        title="Distribution of MFN Tariff",
        title_x=0.30,
        xaxis_title="MFN Tariff (%)",
        yaxis_title="Number of Countries"
    )
    show_chart(fig)
    left, right = st.columns(2)
    with left:
        st.subheader("📊 MFN Tariff by Income Group")
        income_tariff = (
            filtered.groupby("Income_Group")["MFN Simple Average (%)"]
            .mean()
            .reset_index()
            .sort_values("MFN Simple Average (%)", ascending=False)
        )
        fig = px.bar(
            income_tariff,
            x="Income_Group",
            y="MFN Simple Average (%)",
            text="MFN Simple Average (%)",
            color="MFN Simple Average (%)",
            color_continuous_scale="Sunset"   # warm gradient
        )
        fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig.update_layout(
            template="plotly_white",
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            height=500,
            coloraxis_showscale=False,
            xaxis_title="Income Group",
            yaxis_title="Average MFN Tariff (%)"
        )
        show_chart(fig)
    with right:
        st.subheader("🌍 MFN Tariff by Continent")
        continent_tariff = (
            filtered.groupby("Continent")["MFN Simple Average (%)"]
            .mean()
            .reset_index()
            .sort_values("MFN Simple Average (%)", ascending=False)
        )
        fig = px.bar(
            continent_tariff,
            x="Continent",
            y="MFN Simple Average (%)",
            text="MFN Simple Average (%)",
            color="MFN Simple Average (%)",
            color_continuous_scale="Viridis"   # bright green-blue gradient
        )
        fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig.update_layout(
            template="plotly_white",
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            height=500,
            coloraxis_showscale=False,
            xaxis_title="Continent",
            yaxis_title="Average MFN Tariff (%)"
        )
        show_chart(fig)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📊 AHS Tariff Distribution")
        fig = px.histogram(
            filtered,
            x="AHS Simple Average (%)",
            nbins=35,
            color_discrete_sequence=["#00BFFF"]  # bright sky blue
        )
        fig.update_layout(
            template="plotly_white",
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            height=500,
            title="Distribution of AHS Tariff",
            title_x=0.28,
            xaxis_title="AHS Tariff (%)",
            yaxis_title="Frequency"
        )
        show_chart(fig)
    with col2:
        st.subheader("📈 MFN vs AHS Tariff")
        tariff_compare = (
            filtered.groupby("Income_Group")[["MFN Simple Average (%)", "AHS Simple Average (%)"]]
            .mean()
            .reset_index()
        )
        compare = tariff_compare.melt(
            id_vars="Income_Group",
            value_vars=["MFN Simple Average (%)", "AHS Simple Average (%)"],
            var_name="Tariff Type",
            value_name="Average Tariff"
        )
        fig = px.bar(
            compare,
            x="Income_Group",
            y="Average Tariff",
            color="Tariff Type",
            barmode="group",
            text="Average Tariff",
            color_discrete_map={
                "MFN Simple Average (%)": "#FF8C00",  # orange
                "AHS Simple Average (%)": "#00BFFF"   # sky blue
            }
        )
        fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
        fig.update_layout(
            template="plotly_white",
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            height=500,
            title="MFN vs AHS Tariff Comparison",
            title_x=0.22,
            xaxis_title="Income Group",
            yaxis_title="Average Tariff (%)"
        )
        show_chart(fig)
    st.markdown("---")
    st.subheader("🌍 Global MFN Tariff Map")
    world_tariff = (
        filtered.groupby("Country")["MFN Simple Average (%)"]
        .mean()
        .reset_index()
    )
    fig = px.choropleth(
        world_tariff,
        locations="Country",
        locationmode="country names",
        color="MFN Simple Average (%)",
        hover_name="Country",
        color_continuous_scale="YlGnBu",   # yellow-green-blue
        title="Average MFN Tariff by Country"
    )
    fig.update_layout(
        template="plotly_white",
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        height=600,
        title_x=0.28,
        geo=dict(showframe=False, showcoastlines=True, projection_type="natural earth")
    )
    show_chart(fig)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌳 MFN Tariff Treemap")
        tree = (
            filtered.groupby("Country")["MFN Simple Average (%)"]
            .mean()
            .reset_index()
        )
        fig = px.treemap(
            tree,
            path=["Country"],
            values="MFN Simple Average (%)",
            color="MFN Simple Average (%)",
            color_continuous_scale="YlGnBu" 
        )
        fig.update_layout(template="plotly_white", plot_bgcolor="#FFFFFF", paper_bgcolor="#FFFFFF", height=520)
        show_chart(fig)
    with col2:
        st.subheader("🥧 Average AHS Tariff by Continent")
        ahs_continent = (
            filtered.groupby("Continent")["AHS Simple Average (%)"]
            .mean()
            .reset_index()
        )
        fig = px.pie(
            ahs_continent,
            names="Continent",
            values="AHS Simple Average (%)",
            hole=0.55,
            color_discrete_sequence=px.colors.qualitative.Set3   # bright pastel set
        )
        fig.update_layout(template="plotly_white", plot_bgcolor="#FFFFFF", paper_bgcolor="#FFFFFF", height=520)
        show_chart(fig)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📦 Tariff Distribution by Income Group")
        fig = px.box(
            filtered,
            x="Income_Group",
            y="MFN Simple Average (%)",
            color="Income_Group",
            points="outliers",
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig.update_layout(
            template="plotly_white",
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            height=500,
            title="MFN Tariff Spread",
            title_x=0.30,
            xaxis_title="Income Group",
            yaxis_title="MFN Tariff (%)",
            showlegend=False
        )
        show_chart(fig)
    with col2:
        st.subheader("🔵 MFN Tariff vs Export Value")
        fig = px.scatter(
            filtered,
            x="MFN Simple Average (%)",
            y="Export_Value",
            color="Continent",
            size="Import_Value",
            hover_name="Country",
            hover_data=["Year"],
            opacity=0.75,
            color_discrete_sequence=px.colors.qualitative.Set2   # bright categorical colors
        )
        fig.update_layout(
            template="plotly_white",
            plot_bgcolor="#FFFFFF",
            paper_bgcolor="#FFFFFF",
            height=500,
            title="Tariff vs Export Performance",
            title_x=0.25,
            xaxis_title="MFN Tariff (%)",
            yaxis_title="Export Value"
        )
        show_chart(fig)
    st.markdown("---")
    st.subheader("💡 Tariff Insights")
    avg_mfn = filtered["MFN Simple Average (%)"].mean()
    avg_ahs = filtered["AHS Simple Average (%)"].mean()
    highest_income_group = (
        filtered.groupby("Income_Group")["MFN Simple Average (%)"]
        .mean()
        .idxmax()
    )
    lowest_income_group = (
        filtered.groupby("Income_Group")["MFN Simple Average (%)"]
        .mean()
        .idxmin()
    )
    top_country = (
        filtered.groupby("Country")["MFN Simple Average (%)"]
        .mean()
        .idxmax()
    )
    top_country_value = (
        filtered.groupby("Country")["MFN Simple Average (%)"]
        .mean()
        .max()
    )
    a, b, c = st.columns(3)
    with a:
        st.markdown(f"""
        <div class="trade-insight">
        <div class="trade-head">📊 Avg MFN Tariff</div>
        <div class="trade-body">{avg_mfn:.2f}%</div>
        <div class="trade-small">Global Average</div>
        </div>
        """, unsafe_allow_html=True)
    with b:
        st.markdown(f"""
        <div class="trade-insight">
        <div class="trade-head">📊 Avg AHS Tariff</div>
        <div class="trade-body">{avg_ahs:.2f}%</div>
        <div class="trade-small">Global Average</div>
        </div>
        """, unsafe_allow_html=True)
    with c:
        st.markdown(f"""
        <div class="trade-insight">
        <div class="trade-head">🌍 Highest MFN Tariff Country</div>
        <div class="trade-body">{top_country}</div>
        <div class="trade-small">{top_country_value:.2f}%</div>
        </div>
        """, unsafe_allow_html=True)
    d, e = st.columns(2)
    with d:
        st.markdown(f"""
        <div class="trade-insight">
        <div class="trade-head">⬆️ Highest Income Group</div>
        <div class="trade-body">{highest_income_group}</div>
        <div class="trade-small">Highest Avg MFN Tariff</div>
        </div>
        """, unsafe_allow_html=True)
    with e:
        st.markdown(f"""
        <div class="trade-insight">
        <div class="trade-head">⬇️ Lowest Income Group</div>
        <div class="trade-body">{lowest_income_group}</div>
        <div class="trade-small">Lowest Avg MFN Tariff</div>
        </div>
        """, unsafe_allow_html=True)
elif page == '🌍 Geographic Analysis':       
    st.title("🌍 Geographic Analysis")
    st.markdown(
        "<h4 style='section-header'>Global Trade Across Continents & Countries</h4>",
        unsafe_allow_html=True
    )
    filtered["Trade_Volume"] = (
    filtered["Import_Value"] +
    filtered["Export_Value"]
    )
    total_countries = filtered["Country"].nunique()
    total_continents = filtered["Continent"].nunique()
    total_trade = filtered["Trade_Volume"].sum()
    continent_trade = (
        filtered.groupby("Continent")["Trade_Volume"]
        .sum()
    )
    leading_continent = continent_trade.idxmax()
    st.subheader("📊 Geographic Overview")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
            <div class="kpi-label">🌍 Countries</div>
            <div class="kpi-value">{total_countries}</div>
            <div class="kpi-sub">Total in dataset</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="kpi-card accent-emerald">
            <div class="kpi-label">🌎 Continents</div>
            <div class="kpi-value">{total_continents}</div>
            <div class="kpi-sub">Global regions</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="kpi-card accent-gold">
            <div class="kpi-label">📦 Trade Volume</div>
            <div class="kpi-value">${total_trade/1e12:.2f} T</div>
            <div class="kpi-sub">Imports + Exports</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="kpi-card accent-purple">
            <div class="kpi-label">🏆 Leading Continent</div>
            <div class="kpi-value">{leading_continent}</div>
            <div class="kpi-sub">Highest trade volume</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("🌍 Global Trade Map")
    world_trade = (
        filtered.groupby("Country")["Trade_Volume"]
        .sum()
        .reset_index()
    )
    fig = px.choropleth(
        world_trade,
        locations="Country",
        locationmode="country names",
        color="Trade_Volume",
        hover_name="Country",
        color_continuous_scale="Viridis",
        title="Global Trade Volume by Country"
    )
    fig.update_layout(
        template="plotly_white",
        height=620,
        title_x=0.28,
        geo=dict(
            showframe=False,
            showcoastlines=True,
            projection_type="natural earth"
        )
    )
    show_chart(fig)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌎 Trade Volume by Continent")
        continent_df = (
            filtered.groupby("Continent")["Trade_Volume"]
            .sum()
            .reset_index()
            .sort_values(
                "Trade_Volume",
                ascending=False
            )
        )
        fig = px.bar(
            continent_df,
            x="Continent",
            y="Trade_Volume",
            text="Trade_Volume",
            color="Trade_Volume",
            color_continuous_scale="Viridis"
        )
        fig.update_layout(
            template="plotly_white",
            height=500,
            coloraxis_showscale=False,
            xaxis_title="Continent",
            yaxis_title="Trade Volume"
        )
        fig.update_traces(
            texttemplate="$%{text:.2s}",
            textposition="outside"
        )
        show_chart(fig)
    with col2:
        st.subheader("🥧 Trade Share by Continent")
        fig = px.pie(
            continent_df,
            names="Continent",
            values="Trade_Volume",
            hole=0.55,
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_layout(
            template="plotly_white",
            height=500
        )
        show_chart(fig)
    st.markdown("---")
    top_country = (
        filtered.groupby("Country")["Trade_Volume"]
        .sum()
        .reset_index()
        .sort_values(
            "Trade_Volume",
            ascending=False
        )
        .head(15)
    )
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🏆 Top 15 Trading Countries")
        fig = px.bar(
            top_country,
            x="Trade_Volume",
            y="Country",
            orientation="h",
            text="Trade_Volume",
            color="Trade_Volume",
            color_continuous_scale="Blues"
        )
        fig.update_layout(
            template="plotly_white",
            height=550,
            title="Top 15 Countries by Trade Volume",
            title_x=0.25,
            coloraxis_showscale=False,
            yaxis={"categoryorder":"total ascending"},
            xaxis_title="Trade Volume",
            yaxis_title=""
        )
        fig.update_traces(
            texttemplate="$%{text:.2s}",
            textposition="outside"
        )
        show_chart(fig)
    with col2:
        st.subheader("🌳 Trade Contribution Treemap")
        tree = (
            filtered.groupby(
                ["Continent","Country"]
            )["Trade_Volume"]
            .sum()
            .reset_index()
        )
        fig = px.treemap(
            tree,
            path=["Continent","Country"],
            values="Trade_Volume",
            color="Trade_Volume",
            color_continuous_scale="Viridis"
        )
        fig.update_layout(
            template="plotly_white",
            height=550,
            margin=dict(t=40,l=5,r=5,b=5)
        )
        show_chart(fig)
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("☀️ Geographic Hierarchy")
        sun = (
            filtered.groupby(
                ["Continent","Country"]
            )["Trade_Volume"]
            .sum()
            .reset_index()
        )
        fig = px.sunburst(
            sun,
            path=["Continent","Country"],
            values="Trade_Volume",
            color="Trade_Volume",
            color_continuous_scale="Viridis"
        )
        fig.update_layout(
            template="plotly_white",
            height=550
        )
        show_chart(fig)
    with col2:
        st.subheader("📋 Country Trade Summary")
        summary = (
            filtered.groupby("Country")
            .agg(
                Trade_Volume=("Trade_Volume","sum"),
                Import_Value=("Import_Value","sum"),
                Export_Value=("Export_Value","sum")
            )
            .reset_index()
            .sort_values(
                "Trade_Volume",
                ascending=False
            )
            .head(15)
        )
        summary["Trade_Volume"] = summary["Trade_Volume"] / 1e9
        summary["Import_Value"] = summary["Import_Value"] / 1e9
        summary["Export_Value"] = summary["Export_Value"] / 1e9

        summary = summary.rename(columns={
            "Trade_Volume":"Trade (B$)",
            "Import_Value":"Import (B$)",
            "Export_Value":"Export (B$)"
        })
        st.dataframe(
            summary,
            use_container_width=True,
            hide_index=True
        )
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🌐 Global Trade Bubble Chart")
        bubble = (
            filtered.groupby(["Country","Continent"])[
                ["Import_Value","Export_Value","Trade_Volume"]
            ]
            .sum()
            .reset_index()
        )
        fig = px.scatter(
            bubble,
            x="Import_Value",
            y="Export_Value",
            size="Trade_Volume",
            color="Continent",
            hover_name="Country",
            size_max=45
        )
        fig.update_layout(
            template="plotly_white",
            height=520,
            title="Trade Relationship",
            title_x=0.30,
            xaxis_title="Import Value",
            yaxis_title="Export Value"
        )
        show_chart(fig)
    with col2:
        st.subheader("📈 Trade Volume Distribution")
        fig = px.histogram(
            filtered,
            x="Trade_Volume",
            nbins=35,
            color_discrete_sequence=["#1362EB"]
        )
        fig.update_layout(
            template="plotly_white",
            height=520,
            title="Trade Volume Distribution",
            title_x=0.28,
            xaxis_title="Trade Volume",
            yaxis_title="Frequency"
        )
        show_chart(fig)
    st.markdown("---")
    st.subheader("💡 Geographic Insights")
    top_country = (
        filtered.groupby("Country")["Trade_Volume"]
        .sum()
    )
    best_country = top_country.idxmax()
    best_country_value = top_country.max()

    top_continent = (
        filtered.groupby("Continent")["Trade_Volume"]
        .sum()
    )
    best_continent = top_continent.idxmax()
    best_continent_value = top_continent.max()
    st.markdown("""
    <style>
    .geo-insight{
        background:linear-gradient(135deg,#1362EB,#00B4D8);
        color:white;
        border-radius:18px;
        padding:22px;
        text-align:center;
        height:175px;
        box-shadow:0 6px 18px rgba(0,0,0,.18);
    }
    .geo-head{
        font-size:18px;
        font-weight:bold;
    }
    .geo-body{
        font-size:28px;
        margin-top:15px;
        font-weight:bold;

    }
    .geo-small{

        font-size:15px;
        margin-top:10px;

    }
    </style>
    """, unsafe_allow_html=True)
    a, b, c = st.columns(3)
    with a:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
        <div class="geo-insight">

        <div class="geo-head">
        🌎 Leading Continent
        </div>

        <div class="geo-body">
        {best_continent}
        </div>

        <div class="geo-small">
        ${best_continent_value/1e12:.2f} Trillion Trade
        </div>

        </div>
        """, unsafe_allow_html=True)
    with b:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
        <div class="geo-insight">

        <div class="geo-head">
        🏆 Largest Trading Country
        </div>

        <div class="geo-body">
        {best_country}
        </div>

        <div class="geo-small">
        ${best_country_value/1e12:.2f} Trillion Trade
        </div>

        </div>
        """, unsafe_allow_html=True)
    with c:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
        <div class="geo-insight">

        <div class="geo-head">
        📦 Total Trade Volume
        </div>

        <div class="geo-body">
        ${total_trade/1e12:.2f} T
        </div>

        <div class="geo-small">
        Combined Global Imports & Exports
        </div>

        </div>
        """, unsafe_allow_html=True)
elif page == "📊 Growth & Competitiveness":
    st.title("📊 Growth & Competitiveness")
    st.markdown(
        "<h4 style='section-header'>Global Growth Performance Analysis</h4>",
        unsafe_allow_html=True
    )
    avg_country_growth = filtered["Country Growth (%)"].mean()
    avg_world_growth = filtered["World Growth (%)"].mean()
    highest_growth = filtered["Country Growth (%)"].max()
    lowest_growth = filtered["Country Growth (%)"].min()
    st.subheader("📊 Growth Overview")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
            <div class="kpi-label">🌍 Avg Country Growth</div>
            <div class="kpi-value">{avg_country_growth:.2f}%</div>
            <div class="kpi-sub">Across all countries</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="kpi-card accent-emerald">
            <div class="kpi-label">🌎 Avg World Growth</div>
            <div class="kpi-value">{avg_world_growth:.2f}%</div>
            <div class="kpi-sub">Global average</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="kpi-card accent-gold">
            <div class="kpi-label">📈 Highest Growth</div>
            <div class="kpi-value">{highest_growth:.2f}%</div>
            <div class="kpi-sub">Top performing country</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="kpi-card accent-red">
            <div class="kpi-label">📉 Lowest Growth</div>
            <div class="kpi-value">{lowest_growth:.2f}%</div>
            <div class="kpi-sub">Lowest performing country</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("📈 Country Growth Trend")
    growth = (
        filtered.groupby("Year")["Country Growth (%)"]
        .mean()
        .reset_index()
    )
    fig = px.line(
        growth,
        x="Year",
        y="Country Growth (%)",
        markers=True,
        color_discrete_sequence=["#276A83"]
    )
    fig.update_layout(
        template="plotly_white",
        height=500
    )
    show_chart(fig)
    st.subheader("🌍 Country Growth vs World Growth")
    compare = (
        filtered.groupby("Year")[
            ["Country Growth (%)", "World Growth (%)"]
        ]
        .mean()
        .reset_index()
    )
    fig = px.line(
        compare,
        x="Year",
        y=[
            "Country Growth (%)",
            "World Growth (%)"
        ],
        markers=True
    )
    fig.update_layout(
        template="plotly_white",
        height=500
    )
    show_chart(fig)
    st.subheader("🏆 Top 10 Growing Countries")
    top_growth = (
        filtered.groupby("Country")["Country Growth (%)"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )
    fig = px.bar(
        top_growth,
        x="Country",
        y="Country Growth (%)",
        text="Country Growth (%)",
        color="Country Growth (%)",
        color_continuous_scale="Viridis"
    )
    fig.update_layout(
        template="plotly_white",
        height=500,
        coloraxis_showscale=False
    )
    show_chart(fig)
    st.subheader("🌎 Average Growth by Continent")
    continent = (
        filtered.groupby("Continent")["Country Growth (%)"]
        .mean()
        .reset_index()
    )
    fig = px.bar(
        continent,
        x="Continent",
        y="Country Growth (%)",
        color="Country Growth (%)",
        color_continuous_scale="Blues"
    )
    fig.update_layout(
        template="plotly_white",
        height=500,
        coloraxis_showscale=False
    )
    show_chart(fig)
    st.subheader("📊 Growth Distribution")
    fig = px.histogram(
        filtered,
        x="Country Growth (%)",
        nbins=30,
        color_discrete_sequence=["#1362EB"]
    )
    fig.update_layout(
        template="plotly_white",
        height=450
    )
    show_chart(fig)
    st.subheader("📈 Growth vs Export Value")
    fig = px.scatter(
        filtered,
        x="Country Growth (%)",
        y="Export_Value",
        color="Continent",
        size="Import_Value",
        hover_name="Country"
    )
    fig.update_layout(
        template="plotly_white",
        height=500
    )
    show_chart(fig)
    st.subheader("🌍 Growth Map")
    map_df = (
        filtered.groupby("Country")["Country Growth (%)"]
        .mean()
        .reset_index()
    )
    fig = px.choropleth(
        map_df,
        locations="Country",
        locationmode="country names",
        color="Country Growth (%)",
        hover_name="Country",
        color_continuous_scale="Viridis"
    )
    fig.update_layout(
        template="plotly_white",
        height=600
    )
    show_chart(fig)
    st.subheader("🔥 Correlation Analysis")
    corr = filtered[
        [
            "Country Growth (%)",
            "World Growth (%)",
            "Import_Value",
            "Export_Value",
            "MFN Simple Average (%)",
            "AHS Simple Average (%)"
        ]
    ].corr(numeric_only=True)
    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r"
    )
    fig.update_layout(
        template="plotly_white",
        height=500
    )
    show_chart(fig)
    st.subheader("💡 Key Insights")
    best_country = (
        filtered.groupby("Country")["Country Growth (%)"]
        .mean()
        .idxmax()
    )
    best_growth = (
        filtered.groupby("Country")["Country Growth (%)"]
        .mean()
        .max()
    )
    best_year = (
        filtered.groupby("Year")["Country Growth (%)"]
        .mean()
        .idxmax()
    )
    c1, c2 = st.columns(2)
    c1.markdown(
        f"""
        <div class="kpi-card accent-blue">
            <div class="kpi-label">📈 Highest Growth</div>
            <div class="kpi-value">{best_growth:.2f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    c2.markdown(
        f"""
        <div class="kpi-card accent-emerald">
            <div class="kpi-label">📅 Peak Growth Year</div>
            <div class="kpi-value">{best_year}</div>
        </div>
        """,
        unsafe_allow_html=True
    )
elif page == "📙 Dataset":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">📙 Dataset Explorer</div>
        <div class="hero-subtitle">Explore, Understand & Download the Project Datasets</div>
    </div>
    """, unsafe_allow_html=True)
    dataset = st.selectbox(
        "📂 Select Dataset",
        [
            "Merged Dataset",
            "Cleaned_Dataset1",
            "Cleaned_Dataset2"
        ]
    )
    if dataset == "Merged Dataset":
        display_df = merged
    elif dataset == "Cleaned_Dataset1":
        display_df = df
    else:
        display_df = df1
    total_rows = len(display_df)
    total_columns = len(display_df.columns)
    country_count = display_df["Country"].nunique() if "Country" in display_df.columns else 0
    year_range = f"{display_df['Year'].min()} - {display_df['Year'].max()}" if "Year" in display_df.columns else "-"
    st.subheader("📊 Dataset Overview")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
            <div class="kpi-label">📄 Total Records</div>
            <div class="kpi-value">{total_rows:,}</div>
            <div class="kpi-sub">Rows in dataset</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="kpi-card accent-emerald">
            <div class="kpi-label">📑 Total Columns</div>
            <div class="kpi-value">{total_columns}</div>
            <div class="kpi-sub">Features available</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="kpi-card accent-gold">
            <div class="kpi-label">🌍 Countries</div>
            <div class="kpi-value">{country_count}</div>
            <div class="kpi-sub">Unique country entries</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="kpi-card accent-purple">
            <div class="kpi-label">📅 Year Range</div>
            <div class="kpi-value">{year_range}</div>
            <div class="kpi-sub">Available years</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    if "Country" in display_df.columns:
        search = st.text_input("🔍 Search Country")
        if search:
            display_df = display_df[
                display_df["Country"].str.contains(search, case=False, na=False)
            ]
    st.subheader("👀 Dataset Preview")
    st.dataframe(display_df, use_container_width=True, height=450)
    st.subheader("📋 Dataset Information")
    info = pd.DataFrame({
        "Column": display_df.columns,
        "Data Type": display_df.dtypes.astype(str),
        "Missing Values": display_df.isnull().sum().values,
        "Unique Values": display_df.nunique().values
    })
    st.dataframe(info, use_container_width=True)
    st.subheader("📊 Statistical Summary")
    st.dataframe(display_df.describe(include="all"), use_container_width=True)
    st.subheader("❗ Missing Values")
    missing = display_df.isnull().sum().reset_index()
    missing.columns = ["Column", "Missing Values"]
    fig = px.bar(
        missing,
        x="Missing Values",
        y="Column",
        orientation="h",
        color="Missing Values",
        color_continuous_scale="Reds",
        title="Missing Values by Column"
    )
    fig.update_layout(template="plotly_white", height=500, title_x=0.5)
    show_chart(fig)
    st.subheader("🔥 Correlation Heatmap")
    numeric_df = display_df.select_dtypes(include="number")
    if numeric_df.shape[1] > 1:
        fig = px.imshow(
            numeric_df.corr(),
            text_auto=".2f",
            color_continuous_scale="RdBu_r",
            aspect="auto"
        )
        fig.update_layout(template="plotly_white", height=650, title="Correlation Matrix", title_x=0.5)
        show_chart(fig)

    st.subheader("💡 Dataset Insights")
    a, b = st.columns(2)
    with a:
        st.markdown(f"""
        <div class="summary-box">
            ✅ Records : {total_rows:,}<br>
            ✅ Columns : {total_columns}<br>
            ✅ Countries : {country_count}<br>
            ✅ Year Range : {year_range}
        </div>
        """, unsafe_allow_html=True)
    with b:
        st.markdown(f"""
        <div class="summary-box">
            ✔ Missing Values : {display_df.isnull().sum().sum()}<br>
            ✔ Duplicate Rows : {display_df.duplicated().sum()}<br>
            ✔ Numeric Columns : {len(display_df.select_dtypes(include='number').columns)}<br>
            ✔ Categorical Columns : {len(display_df.select_dtypes(exclude='number').columns)}
        </div>
        """, unsafe_allow_html=True)

    st.subheader("⬇ Download Dataset")
    csv = display_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f"{dataset.replace(' ','_')}.csv",
        mime="text/csv"
    )
elif page == "⚙️ Pre Processing":
    st.markdown("""
    <div class="hero-banner">
        <div class="hero-title">⚙️ Data Pre-Processing Dashboard</div>
        <div class="hero-subtitle">Cleaning • Validation • Transformation • Quality Assessment</div>
    </div>
    """, unsafe_allow_html=True)
    total_rows = merged.shape[0]
    total_columns = merged.shape[1]
    duplicate_rows = merged.duplicated().sum()
    missing_values = merged.isnull().sum().sum()
    unique_countries = merged["Country"].nunique()
    quality_score = ((1 - (missing_values / (total_rows * total_columns))) * 100)
    st.subheader("📊 Dataset Overview")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.markdown(f"""
        <div class="kpi-card accent-blue">
            <div class="kpi-label">📄 Total Records</div>
            <div class="kpi-value">{total_rows:,}</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="kpi-card accent-emerald">
            <div class="kpi-label">📑 Columns</div>
            <div class="kpi-value">{total_columns}</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="kpi-card accent-gold">
            <div class="kpi-label">🌍 Countries</div>
            <div class="kpi-value">{unique_countries}</div>
        </div>
        """, unsafe_allow_html=True)
    with c4:
        st.markdown(f"""
        <div class="kpi-card accent-red">
            <div class="kpi-label">❗ Missing</div>
            <div class="kpi-value">{missing_values}</div>
        </div>
        """, unsafe_allow_html=True)
    with c5:
        st.markdown(f"""
        <div class="kpi-card accent-purple">
            <div class="kpi-label">🗑 Duplicates</div>
            <div class="kpi-value">{duplicate_rows}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("⭐ Dataset Quality Score")
    st.progress(int(quality_score))
    col1, col2 = st.columns([1, 2])
    with col1:
        st.metric("Quality Score", f"{quality_score:.2f}%")
    with col2:
        if quality_score >= 95:
            st.success("Excellent dataset quality. Ready for advanced analytics.")
        elif quality_score >= 85:
            st.warning("Good quality dataset with minor missing information.")
        else:
            st.error("Dataset requires further cleaning.")
    st.markdown("---")
    st.subheader("❗ Missing Values Analysis")
    missing_df = merged.isnull().sum().reset_index()
    missing_df.columns = ["Column", "Missing Values"]
    missing_df = missing_df[missing_df["Missing Values"] > 0]
    if len(missing_df) > 0:
        with st.container():
            st.markdown('<div class="chart-card">', unsafe_allow_html=True)
            missing_df = merged.isnull().sum().reset_index()
            missing_df.columns = ["Column", "Missing Values"]
            fig = px.bar(
                missing_df,
                x="Column",
                y="Missing Values",
                color="Missing Values",
                text="Missing Values",
                color_continuous_scale="Reds",
                title="Missing Values by Column"
            )
            fig.update_layout(template="plotly_white", height=500, title_x=0.25, coloraxis_showscale=False)
            fig.update_traces(textposition="outside")
            show_chart(fig)
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.success("✅ No Missing Values Found in Dataset")
    st.markdown("---")
    st.subheader("📊 Data Types & Missing Value Pattern")
    left, right = st.columns(2)
    with left:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        dtype_df = merged.dtypes.astype(str).value_counts().reset_index()
        dtype_df.columns = ["Data Type", "Count"]
        fig = px.pie(
            dtype_df,
            names="Data Type",
            values="Count",
            hole=0.55,
            title="Column Data Types",
            color_discrete_sequence=px.colors.qualitative.Set2
        )
        fig.update_layout(template="plotly_white", height=500, title_x=0.25)
        show_chart(fig)
        st.markdown('</div>', unsafe_allow_html=True)
    with right:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        fig = px.imshow(
            merged.isnull(),
            aspect="auto",
            color_continuous_scale=["#FFFFFF", "#1362EB"]
        )
        fig.update_layout(template="plotly_white", title="Missing Value Heatmap", title_x=0.25, height=500, coloraxis_showscale=False)
        show_chart(fig)
        st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("🧹 Data Cleaning Pipeline")
    pipeline = [
        "Loaded Dataset 1",
        "Loaded Dataset 2",
        "Merged Both Datasets",
        "Checked Missing Values",
        "Removed Duplicate Records",
        "Validated Data Types",
        "Standardized Country Names",
        "Verified Numeric Columns",
        "Generated Final Clean Dataset"
    ]
    for step in pipeline:
        st.markdown(f"""
        <div class="summary-box">
            ✅ {step} <span style="color:#00C853;font-weight:bold;float:right;">Completed</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("📋 Dataset Summary")
    summary = pd.DataFrame({
        "Column": merged.columns,
        "Data Type": merged.dtypes.astype(str),
        "Missing Values": merged.isnull().sum().values,
        "Unique Values": merged.nunique().values
    })
    st.dataframe(summary, use_container_width=True, hide_index=True)
    st.markdown("---")
    st.subheader("📈 Statistical Summary")
    st.dataframe(merged.describe(), use_container_width=True)
    st.markdown("---")
    st.subheader("👀 Dataset Preview")
    with st.expander("Click to View Clean Dataset", expanded=False):
        st.dataframe(merged.head(20), use_container_width=True, height=500)
    st.markdown("---")
    st.subheader("⬇ Download Clean Dataset")
    csv = merged.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Merged Clean Dataset",
        data=csv,
        file_name="Merged_Cleaned_Dataset.csv",
        mime="text/csv"
    )
    st.markdown("---")
    st.subheader("🎯 Processing Status")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.success("✔ Missing Values Checked")
    with c2: st.success("✔ Duplicates Removed")
    with c3: st.success("✔ Dataset Validated")
    with c4: st.success("✔ Ready for Analytics")
    st.markdown("---")
    st.markdown("""
    <div class="hero-banner">
        <h3>✅ Data Processing Completed Successfully</h3>
        <p>The dataset has been cleaned, validated, standardized, and prepared for visualization and advanced trade analytics.</p>
    </div>
    """, unsafe_allow_html=True)
elif page == "👤 About":
    st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">🌍 World Import & Export Trade Analysis Dashboard</h1>
        <h4 class="hero-subtitle">Interactive Business Intelligence Dashboard using Streamlit & Plotly</h4>
        <div class="hero-tags">
            <span class="tag">1990–2023</span>
            <span class="tag">190+ Countries</span>
            <span class="tag">Trade • Tariffs • Growth</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="summary-box">
        <h3 class="section-header">📌 Project Overview</h3>
        <p style="color:#F8FAFC;">
        This dashboard provides a comprehensive analysis of global import and export trade.
        It enables users to explore international trade patterns, compare imports and exports,
        analyze tariff structures, evaluate country competitiveness, and monitor global trade
        performance using interactive visualizations.
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<h3 class='section-header'>🎯 Project Objectives</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='analytics-card'><div class='analytics-title'>Analyze Global Trade</div></div>", unsafe_allow_html=True)
        st.markdown("<div class='analytics-card'><div class='analytics-title'>Compare Imports & Exports</div></div>", unsafe_allow_html=True)
        st.markdown("<div class='analytics-card'><div class='analytics-title'>Study Tariff Policies</div></div>", unsafe_allow_html=True)
        st.markdown("<div class='analytics-card'><div class='analytics-title'>Evaluate Country Competitiveness</div></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='analytics-card'><div class='analytics-title'>Geographic Trade Analysis</div></div>", unsafe_allow_html=True)
        st.markdown("<div class='analytics-card'><div class='analytics-title'>Detect Trade Growth Trends</div></div>", unsafe_allow_html=True)
        st.markdown("<div class='analytics-card'><div class='analytics-title'>Interactive Data Exploration</div></div>", unsafe_allow_html=True)
        st.markdown("<div class='analytics-card'><div class='analytics-title'>Data Driven Decision Making</div></div>", unsafe_allow_html=True)
    st.markdown("---")
    left, right = st.columns(2)
    with left:
        st.markdown("<h3 class='section-header'>🛠 Technologies Used</h3>", unsafe_allow_html=True)
        tech = pd.DataFrame({
            "Technology": [
                "Python",
                "Pandas",
                "NumPy",
                "Streamlit",
                "Plotly",
                "HTML/CSS"
            ]
        })
        st.dataframe(tech, hide_index=True, use_container_width=True)
    with right:
        st.markdown("<h3 class='section-header'>📂 Dataset Information</h3>", unsafe_allow_html=True)
        st.info(f"""
        📊 Dataset 1 : Trade Indicators  
        📊 Dataset 2 : Import & Export Statistics  
        📈 Total Records : {merged.shape[0]:,}  
        🧾 Total Columns : {merged.shape[1]}  
        🌍 Countries Covered : {merged['Country'].nunique()}
        """)
        st.markdown("---")
    st.markdown("<h3 class='section-header'>✨ Dashboard Features</h3>", unsafe_allow_html=True)
    features = [
        "Interactive KPI Cards",
        "Import Analytics",
        "Export Analytics",
        "Trade Comparison",
        "Tariff Analysis",
        "Geographical Analysis",
        "Growth & Competitiveness",
        "Dataset Explorer",
        "Data Pre-processing",
        "Download Dataset"
    ]
    for feature in features:
        st.markdown(f"<div class='insight-card'><div class='insight-title'>{feature}</div></div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h3 class='section-header'>📊 Dashboard Workflow</h3>", unsafe_allow_html=True)
    workflow_steps = [
        "📥 Data Collection",
        "🧹 Data Cleaning",
        "🔄 Data Processing",
        "📊 Visualization",
        "📈 Analysis",
        "📋 Insights"
    ]
    for step in workflow_steps:
        st.markdown(f"<div class='workflow-step' style='color:#F8FAFC;'>{step}</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("<h3 class='section-header'>👨‍🎓 Developed By</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="insight-card">
        <div class="insight-title">Name</div>
        <div class="insight-value">Komal Sharma</div>
        <div class="insight-text">Project: World Import & Export Trade Analysis Dashboard</div>
        <div class="insight-text">Tools: Python • Pandas • Streamlit • Plotly</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    st.success("🎉 Thank you for exploring the World Import & Export Trade Analysis Dashboard!")
    st.markdown("<div class='dashboard-footer'>© 2026 | Developed using Streamlit & Plotly</div>", unsafe_allow_html=True)

    import streamlit as st
    from openai import OpenAI
    with st.sidebar:
        api_key = st.text_input("OpenAI API Key", type="password")
elif page == "🤖 ChatBot":
    st.title("Chat bot")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if prompt := st.chat_input("How can I help you?"):
        if not api_key:
            st.warning("Please enter your API key in the sidebar.")
            st.stop()
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        client = OpenAI(api_key=api_key)
        with st.chat_message("assistant"):
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            )
            reply = response.choices[0].message.content
            st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})
        