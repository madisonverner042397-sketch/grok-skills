---
name: testing-automation-agent
description: 'Build a test automation strategy: generated unit, integration and load tests, performance benchmarks, a quality dashboard and a CI pipeline. Use when setting up or scaling automated testing for a project.'
license: MIT
---

# Testing Automation Agent 🧪

> **Note:** Some code here is an architecture sketch: classes may call helpers that aren't defined in this file. Treat those as outlines to implement, not drop-in code. Any `grok --agent ...` commands come from the source repo; check your CLI's docs before relying on them.

> AI-powered testing automation that ensures code quality through physics-inspired precision testing

## 🎯 Why This Matters for Grok

Grok's analytical precision and efficiency focus create perfect testing automation:

- **Systematic Coverage** 🎯: Physics-inspired comprehensive testing
- **Automated Generation** 🤖: AI-powered test creation
- **Real-time Validation** ⚡: Instant feedback and corrections
- **Quality Optimization** 📈: Continuous improvement loop

## 🛠️ Core Capabilities

### 1. Test Generation
- Unit tests: auto_generated
- Integration tests: comprehensive
- E2E tests: intelligent
- Performance tests: automated
- Security tests: integrated

### 2. Test Execution
- Parallel execution: optimized
- Cross-platform: comprehensive
- Continuous integration: seamless
- Real-time reporting: detailed
- Failure analysis: automated

### 3. Quality Assurance
- Code coverage: comprehensive
- Performance benchmarking: continuous
- Security scanning: automated
- Accessibility testing: integrated
- User experience validation: automated

## 🧪 Testing Frameworks

### AI Test Generation
```python
class TestGenerator:
    def __init__(self):
        self.test_patterns = {
            'unit_tests': self.generate_unit_tests,
            'integration_tests': self.generate_integration_tests,
            'e2e_tests': self.generate_e2e_tests,
            'performance_tests': self.generate_performance_tests
        }
    
    def generate_unit_tests(self, function_code):
        """Generate comprehensive unit tests for given function"""
        
        # Analyze function signature and logic
        function_analysis = self.analyze_function(function_code)
        
        test_cases = []
        
        # Generate normal cases
        for normal_case in function_analysis['normal_cases']:
            test_case = {
                'description': f"Test with normal input: {normal_case['description']}",
                'input': normal_case['input'],
                'expected': normal_case['expected'],
                'test_type': 'normal'
            }
            test_cases.append(test_case)
        
        # Generate edge cases
        for edge_case in function_analysis['edge_cases']:
            test_case = {
                'description': f"Test edge case: {edge_case['description']}",
                'input': edge_case['input'],
                'expected': edge_case['expected'],
                'test_type': 'edge'
            }
            test_cases.append(test_case)
        
        # Generate error cases
        for error_case in function_analysis['error_cases']:
            test_case = {
                'description': f"Test error case: {error_case['description']}",
                'input': error_case['input'],
                'expected_exception': error_case['exception'],
                'test_type': 'error'
            }
            test_cases.append(test_case)
        
        return {
            'function_name': function_analysis['name'],
            'test_cases': test_cases,
            'generated_tests': self.create_test_code(function_analysis, test_cases)
        }
    
    def generate_integration_tests(self, api_endpoint, documentation):
        """Generate integration tests for API endpoints"""
        
        test_scenarios = [
            {
                'scenario': 'Successful request',
                'method': 'GET',
                'endpoint': api_endpoint,
                'expected_status': 200,
                'validation_rules': ['response_schema', 'response_time']
            },
            {
                'scenario': 'Not found',
                'method': 'GET',
                'endpoint': f"{api_endpoint}/999999",
                'expected_status': 404,
                'validation_rules': ['error_response']
            },
            {
                'scenario': 'Invalid authentication',
                'method': 'GET',
                'endpoint': api_endpoint,
                'headers': {'Authorization': 'invalid_token'},
                'expected_status': 401,
                'validation_rules': ['error_response']
            }
        ]
        
        return {
            'endpoint': api_endpoint,
            'test_scenarios': test_scenarios,
            'generated_tests': self.create_integration_test_code(test_scenarios)
        }
```

### Performance Testing
```python
class PerformanceTester:
    def __init__(self):
        self.benchmarks = {
            'response_time': {'excellent': 100, 'good': 500, 'acceptable': 1000},  # ms
            'throughput': {'excellent': 1000, 'good': 500, 'acceptable': 100},    # req/s
            'cpu_usage': {'excellent': 50, 'good': 70, 'acceptable': 85},          # %
            'memory_usage': {'excellent': 512, 'good': 1024, 'acceptable': 2048}   # MB
        }
    
    def run_performance_test(self, test_config):
        """Run comprehensive performance tests"""
        
        results = {}
        
        # Response Time Test
        response_time_results = self.test_response_time(test_config['endpoint'], test_config['requests'])
        results['response_time'] = {
            'mean': response_time_results['mean'],
            'p95': response_time_results['p95'],
            'p99': response_time_results['p99'],
            'rating': self.rate_performance(response_time_results['p95'], 'response_time')
        }
        
        # Throughput Test
        throughput_results = self.test_throughput(test_config['endpoint'], test_config['duration'])
        results['throughput'] = {
            'requests_per_second': throughput_results['rps'],
            'rating': self.rate_performance(throughput_results['rps'], 'throughput')
        }
        
        # Resource Usage Test
        resource_results = self.test_resource_usage(test_config['endpoint'])
        results['resource_usage'] = {
            'cpu_percentage': resource_results['cpu'],
            'memory_mb': resource_results['memory'],
            'cpu_rating': self.rate_performance(resource_results['cpu'], 'cpu_usage'),
            'memory_rating': self.rate_performance(resource_results['memory'], 'memory_usage')
        }
        
        # Overall Performance Score
        overall_score = self.calculate_overall_performance_score(results)
        
        return {
            'test_results': results,
            'overall_score': overall_score,
            'recommendations': self.generate_performance_recommendations(results),
            'baseline_comparison': self.compare_with_baseline(results)
        }
    
    def generate_load_test(self, target_endpoint, user_scenarios):
        """Generate realistic load test scenarios"""
        
        load_test_config = {
            'endpoint': target_endpoint,
            'scenarios': [],
            'ramp_up_time': 300,  # 5 minutes
            'steady_state_time': 600,  # 10 minutes
            'ramp_down_time': 300,  # 5 minutes
            'max_users': 1000
        }
        
        # Convert user scenarios to load test
        for scenario in user_scenarios:
            load_scenario = {
                'name': scenario['name'],
                'weight': scenario['frequency'],
                'requests': scenario['requests'],
                'think_time': scenario.get('think_time', 1.0)
            }
            load_test_config['scenarios'].append(load_scenario)
        
        return {
            'config': load_test_config,
            'jmx_script': self.generate_jmx_script(load_test_config),
            'k6_script': self.generate_k6_script(load_test_config),
            'gatling_script': self.generate_gatling_script(load_test_config)
        }
```

## 📊 Quality Metrics Dashboard

### Real-time Test Results
```javascript
const TestQualityDashboard = {
  testResults: {
    unit_tests: {
      total: 1250,
      passed: 1235,
      failed: 15,
      skipped: 0,
      coverage: 87.5,
      execution_time: 45  // seconds
    },
    
    integration_tests: {
      total: 340,
      passed: 332,
      failed: 8,
      skipped: 0,
      coverage: 72.3,
      execution_time: 120
    },
    
    e2e_tests: {
      total: 85,
      passed: 82,
      failed: 3,
      skipped: 0,
      coverage: 65.8,
      execution_time: 380
    },
    
    performance_tests: {
      total: 25,
      passed: 23,
      failed: 2,
      skipped: 0,
      benchmarks_met: 92,
      execution_time: 900
    }
  },
  
  calculateOverallQualityScore: function() {
    const unitScore = (this.testResults.unit_tests.passed / this.testResults.unit_tests.total) * 100;
    const integrationScore = (this.testResults.integration_tests.passed / this.testResults.integration_tests.total) * 100;
    const e2eScore = (this.testResults.e2e_tests.passed / this.testResults.e2e_tests.total) * 100;
    const performanceScore = this.testResults.performance_tests.benchmarks_met;
    
    const coverageBonus = Math.max(0, Math.min(10, (this.testResults.unit_tests.coverage - 80) / 2));
    
    return {
      overall: (unitScore * 0.3 + integrationScore * 0.3 + e2eScore * 0.2 + performanceScore * 0.2) + coverageBonus,
      breakdown: {
        unit_tests: unitScore,
        integration_tests: integrationScore,
        e2e_tests: e2eScore,
        performance_tests: performanceScore,
        coverage: this.testResults.unit_tests.coverage
      }
    };
  },
  
  generateQualityAlerts: function() {
    const alerts = [];
    const results = this.testResults;
    
    // Coverage alerts
    if (results.unit_tests.coverage < 80) {
      alerts.push({
        level: 'warning',
        type: 'coverage',
        message: `Unit test coverage is low: ${results.unit_tests.coverage}%`,
        recommendation: 'Add more unit tests to reach 80% coverage'
      });
    }
    
    // Failure rate alerts
    const totalFailures = results.unit_tests.failed + results.integration_tests.failed + results.e2e_tests.failed;
    const totalTests = results.unit_tests.total + results.integration_tests.total + results.e2e_tests.total;
    const failureRate = (totalFailures / totalTests) * 100;
    
    if (failureRate > 2) {
      alerts.push({
        level: 'error',
        type: 'failures',
        message: `High failure rate: ${failureRate.toFixed(1)}%`,
        recommendation: 'Review and fix failing tests before deployment'
      });
    }
    
    // Performance alerts
    if (results.performance_tests.benchmarks_met < 90) {
      alerts.push({
        level: 'warning',
        type: 'performance',
        message: `Performance benchmarks not fully met: ${results.performance_tests.benchmarks_met}%`,
        recommendation: 'Optimize code and re-run performance tests'
      });
    }
    
    return alerts;
  }
};
```

## 🔧 Automated Test Execution

### CI/CD Pipeline Integration
```yaml
# .github/workflows/automated-testing.yml
name: Automated Testing Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [20.x, 22.x]
        
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          
      - name: Install dependencies
        run: npm ci
        
      - name: Generate tests
        run: |
          # No published grok-test-generator package exists: generate tests with your agent and commit them
          echo "tests are committed to the repo"
          
      - name: Run unit tests
        run: |
          npm run test:unit -- --coverage --watchAll=false
          
      - name: Run integration tests
        run: |
          npm run test:integration
          
      - name: Upload coverage
        uses: codecov/codecov-action@v5
        with:
          token: ${{ secrets.CODECOV_TOKEN }}
        
      - name: Run performance tests
        run: |
          npm run test:performance
          
      - name: Generate test report
        run: |
          # Use your runner's reporter (e.g. jest-html-reporters, pytest-html) to write test-report.html
          echo "configure an HTML reporter"
          
      - name: Upload test artifacts
        uses: actions/upload-artifact@v4
        with:
          name: test-results
          path: |
            coverage/
            test-report.html
```

## 🎯 Implementation Roadmap

### Phase 1: Foundation (Week 1-2)
- [ ] Basic test generation framework
- [ ] Unit test automation
- [ ] CI/CD integration
- [ ] Basic reporting

### Phase 2: Intelligence (Week 3-4)
- [ ] AI-powered test generation
- [ ] Integration test automation
- [ ] Performance testing framework
- [ ] Advanced reporting

### Phase 3: Advanced (Week 5-6)
- [ ] E2E test automation
- [ ] Security testing integration
- [ ] Accessibility testing
- [ ] Predictive test maintenance

## 📊 Success Metrics

### Testing Excellence
```yaml
quality_metrics:
  test_coverage: "> 85%"
  test_pass_rate: "> 95%"
  automation_level: "90%"
  execution_time: "< 10 minutes"
  
performance_metrics:
  test_execution_speed: "< 30 seconds"
  parallel_efficiency: "> 80%"
  resource_usage: "< 50% CPU"
  reliability: "99.9%"
  
developer_experience:
  test_generation_time: "< 5 minutes"
  debugging_time: "-70%"
  onboarding_time: "-50%"
  satisfaction_score: "> 4.5/5"
```

---

*Ensure code quality through AI-powered testing automation that catches bugs before they reach production.* 🧪✨

---

_Imported from [Awesome Grok Skills](https://github.com/LifeJiggy/Awesome-Grok-Skills) and adapted for this catalog (format and code fixes). Copyright (c) 2024 Awesome Grok Skills. MIT License._
