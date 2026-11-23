---
name: ecommerce-automation-agent
description: 'Automate an online store: catalog, pricing, inventory forecasting, cart recovery, marketing, fraud screening and compliance across Shopify, WooCommerce and marketplaces. Use when planning e-commerce automation or pricing and stock logic.'
license: MIT
---

# E-commerce Automation Agent 🛒

> **Note:** Some code here is an architecture sketch: classes may call helpers that aren't defined in this file. Treat those as outlines to implement, not drop-in code. Any `grok --agent ...` commands come from the source repo; check your CLI's docs before relying on them.

> Automate and optimize your entire e-commerce operation with Grok's efficiency-first approach

## 🎯 Why This Matters for Grok

Grok's optimization expertise transforms chaotic e-commerce operations into streamlined, profitable systems:

- **Maximum Efficiency** ⚡: Reduce manual tasks by 80%
- **Real-time Analytics** 📊: Instant insights from sales data
- **Customer Experience** 😊: Personalized shopping journeys
- **Inventory Optimization** 📦: Smart stock management

## 🛠️ Core Capabilities

### 1. Product Management
```yaml
product_automation:
  - auto_categorization: true
  - price_optimization: dynamic_pricing
  - inventory_tracking: real_time
  - description_generation: ai_powered
```

### 2. Customer Journey Optimization
```yaml
customer_experience:
  - personalized_recommendations: true
  - abandoned_cart_recovery: automated
  - customer_segmentation: behavioral
  - support_automation: 24/7
```

### 3. Marketing Automation
```yaml
marketing_workflows:
  - email_campaigns: triggered
  - social_media_posts: scheduled
  - seo_optimization: continuous
  - conversion_tracking: comprehensive
```

## 📊 Integration Ecosystem

### Platform Support
- **Shopify**: Full API integration
- **WooCommerce**: WordPress e-commerce
- **Amazon**: Seller Central automation
- **Etsy**: Handmade goods optimization
- **Custom Solutions**: Headless commerce support

### Payment Processing
```javascript
// Example rates only: fees vary by country, plan and payment type. Check current pricing.
const paymentGateways = {
  stripe: { fee_percent: 2.9, fee_fixed: 0.30 },
  paypal: { fee_percent: 2.7, fee_fixed: 0.30 },
  square: { fee_percent: 2.6, fee_fixed: 0.10 },
  crypto: { fee_percent: 0.5, fee_fixed: 0 }
};
```

## 🚀 Implementation Workflow

### Phase 1: Discovery (Day 1-3)
1. **Current State Analysis**
   - Inventory audit
   - Sales funnel mapping
   - Technology stack review
   - Process documentation

2. **Goal Setting**
   - Revenue targets
   - Customer satisfaction KPIs
   - Operational efficiency metrics
   - Growth projections

### Phase 2: Automation Setup (Day 4-10)
1. **Backend Integration**
   - API connections
   - Data synchronization
   - Workflow triggers
   - Error handling

2. **Frontend Optimization**
   - Product page enhancements
   - Checkout streamlining
   - Mobile responsiveness
   - Performance optimization

### Phase 3: Intelligence Layer (Day 11-20)
1. **Analytics Implementation**
   - Sales tracking
   - Customer behavior analysis
   - Market trend monitoring
   - Competitor intelligence

2. **AI Integration**
   - Product recommendations
   - Price optimization algorithms
   - Inventory forecasting
   - Customer lifetime value prediction

## 📈 Performance Metrics

### Key Indicators
```yaml
success_metrics:
  revenue_growth: "+25% in 90 days"
  conversion_rate: "from 2% to 4%"
  customer_retention: "+40% improvement"
  operational_costs: "-60% reduction"
  inventory_turnover: "+50% faster"
```

### Real-time Dashboard
```javascript
const ecommerceDashboard = {
  sales: {
    today: 12500,
    week: 87500,
    month: 350000,
    growth: "+12.5%"
  },
  customers: {
    new: 147,
    returning: 89,
    lifetime_value: 450,
    satisfaction: 4.7
  },
  products: {
    total: 1247,
    low_stock: 23,
    best_sellers: ["product_123", "product_456"],
    returns: "2.3%"
  }
};
```

## 🔧 Automation Scripts

### Dynamic Pricing Engine
```python
class DynamicPricing:
    def __init__(self, base_price, unit_cost, min_margin=0.2):
        self.base_price = base_price
        self.unit_cost = unit_cost
        self.min_margin = min_margin
        
    def calculate_optimal_price(self, demand_score, competitor_prices, inventory_level):
        # Demand-based adjustment
        demand_multiplier = 1 + (demand_score - 0.5) * 0.3
        
        # Competitor positioning
        avg_competitor = sum(competitor_prices) / len(competitor_prices)
        price_adjustment = max(-0.15, min(0.15, (avg_competitor - self.base_price) / self.base_price))
        
        # Inventory pressure
        inventory_multiplier = 1.0
        if inventory_level < 0.1:  # Low stock
            inventory_multiplier = 1.1  # Raise price
        elif inventory_level > 0.8:  # High stock
            inventory_multiplier = 0.95  # Lower price
            
        optimal_price = self.base_price * demand_multiplier * (1 + price_adjustment) * inventory_multiplier
        
        # Enforce minimum margin over unit cost: margin = (price - cost) / price
        floor_price = self.unit_cost / (1 - self.min_margin)
        return round(max(optimal_price, floor_price), 2)
```

### Inventory Forecasting
```python
import numpy as np
from sklearn.linear_model import LinearRegression

class InventoryForecaster:
    def __init__(self):
        self.model = LinearRegression()
        
    def train(self, historical_sales, features):
        """Train on historical sales data"""
        X = np.array(features)  # [day_of_week, month, promotions, etc.]
        y = np.array(historical_sales)
        self.model.fit(X, y)
        
    def forecast_demand(self, future_features, days=30):
        """Forecast demand for next N days"""
        forecasts = []
        for day_features in future_features:
            prediction = self.model.predict([day_features])[0]
            forecasts.append(max(0, int(prediction)))
        return forecasts
    
    def calculate_reorder_point(self, future_features, lead_time_days, safety_stock_days=7):
        """Calculate optimal reorder point"""
        daily_forecasts = self.forecast_demand(future_features)
        avg_daily_demand = sum(daily_forecasts) / len(daily_forecasts)
        
        reorder_point = (avg_daily_demand * lead_time_days) + (avg_daily_demand * safety_stock_days)
        return int(reorder_point)
```

## 🎯 Example Scenarios (illustrative, not real customers)

### Case Study: Fashion Retailer
**Challenge**: Manual inventory management, abandoned cart rate 75%
**Solution**: Full automation implementation
**Results**:
- Revenue increase: 45%
- Abandoned cart recovery: 65% → 25%
- Inventory costs: -40%
- Customer satisfaction: 4.2 → 4.8

### Case Study: Electronics Store
**Challenge**: Price monitoring across 50+ competitors
**Solution**: AI-powered dynamic pricing
**Results**:
- Profit margin optimization: +15%
- Price competitiveness: Top 3 in 90% of products
- Manual work reduction: 25 hours/week
- Market share growth: 8%

## 🔍 Market Intelligence

### Competitor Monitoring
```javascript
const competitorTracking = {
  priceMonitoring: {
    frequency: "hourly",
    competitors: ["amazon", "bestbuy", "target"],
    alerts: {
      price_drop: 5,  // Alert if competitor drops price by 5%
      stock_out: true,  // Alert when competitor out of stock
      new_product: true  // Alert for new competitor products
    }
  },
  
  trendAnalysis: {
    social_media: ["twitter", "instagram", "tiktok"],
    search_trends: "google_trends_api",
    market_reports: "industry_analysts"
  }
};
```

### Seasonal Optimization
```python
class SeasonalOptimizer:
    def __init__(self):
        self.seasonal_patterns = {
            "winter": {
                "products": ["heating", "clothing", "holidays"],
                "price_adjustment": 1.1,
                "marketing_focus": "gift_guides"
            },
            "summer": {
                "products": ["outdoor", "travel", "sports"],
                "price_adjustment": 0.95,
                "marketing_focus": "vacation"
            }
        }
    
    def get_seasonal_recommendations(self, current_season):
        pattern = self.seasonal_patterns.get(current_season, {})
        return {
            "featured_products": pattern.get("products", []),
            "price_strategy": pattern.get("price_adjustment", 1.0),
            "campaign_themes": pattern.get("marketing_focus", "general")
        }
```

## 🛡️ Compliance & Security

### Data Protection
```yaml
compliance_framework:
  gdpr:
    consent_management: automated
    data_portability: customer_portal
    right_to_deletion: 30_day_deletion
    
  pci_dss:
    payment_processing: tokenization
    data_storage: encrypted
    access_logs: comprehensive
    
  accessibility:
    wcag_level: AA
    screen_reader_support: true
    keyboard_navigation: full
```

### Fraud Prevention
```python
class FraudDetector:
    def __init__(self):
        self.risk_indicators = {
            "high_risk_countries": ["XX"],
            "velocity_threshold": 5,  # orders per hour
            "suspicious_patterns": ["card_testing", "account_takeover"]
        }
    
    def assess_transaction_risk(self, transaction):
        risk_score = 0
        
        # IP geolocation check
        if transaction.ip_country in self.risk_indicators["high_risk_countries"]:
            risk_score += 30
            
        # Order velocity check
        recent_orders = self.get_recent_orders(transaction.customer_id, hours=1)
        if len(recent_orders) > self.risk_indicators["velocity_threshold"]:
            risk_score += 25
            
        # Payment method analysis
        if self.is_suspicious_payment_method(transaction.payment):
            risk_score += 20
            
        return risk_score
    
    def recommend_action(self, risk_score):
        if risk_score >= 70:
            return "block"
        elif risk_score >= 40:
            return "manual_review"
        else:
            return "approve"
```

## 🚀 Getting Started

### Quick Setup Checklist
- [ ] E-commerce platform integration
- [ ] Payment gateway configuration
- [ ] Inventory system connection
- [ ] Customer data import
- [ ] Analytics implementation
- [ ] Automation workflows setup
- [ ] Testing and validation

### Timeline Expectations
- **Week 1**: Platform integration and data sync
- **Week 2**: Core automation workflows
- **Week 3**: AI optimization features
- **Week 4**: Analytics and reporting
- **Week 5-6**: Testing and refinement

---

*Transform your e-commerce operation from manual labor to automated excellence. Let Grok handle the optimization while you focus on growth!* 🛒✨

---

_Imported from [Awesome Grok Skills](https://github.com/LifeJiggy/Awesome-Grok-Skills) and adapted for this catalog (format and code fixes). Copyright (c) 2024 Awesome Grok Skills. MIT License._
