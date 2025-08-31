# Unified Customer-360 Platform - Project Scaffold

## Architecture: Event-Driven Data Fabric with Regional Compliance Zones

## Technology Stack: Apache Kafka + Debezium CDC + Kubernetes + Multi-Cloud API Gateway

## Directory Structure

```
unified-customer-360/
├── core/
│   ├── customer-domain/
│   │   ├── CustomerAggregate.java         // Event-sourced customer domain model
│   │   ├── CustomerProjection.java        // CQRS read-side projections
│   │   └── CustomerEventStore.java        // Event sourcing implementation
│   ├── compliance-engine/
│   │   ├── RegionalComplianceRules.java   // GDPR, CCPA, APAC compliance logic
│   │   ├── DataLineageTracker.java        // Audit trail and lineage tracking
│   │   └── ConsentManager.java            // Customer consent and right-to-forget
│   └── federation-layer/
│       ├── FederatedQueryEngine.java      // Cross-region query coordination
│       ├── DataResidencyEnforcer.java     // Ensures data stays in region
│       └── ConsistencyManager.java        // Eventual consistency coordination
├── connectors/
│   ├── mainframe-cdc/
│   │   ├── CobolDataExtractor.java        // CDC from mainframe systems
│   │   ├── IBMConnectDirectAdapter.java   // Mainframe integration adapter
│   │   └── LegacyTransactionParser.java   // Parse COBOL transaction formats
│   ├── azure-streaming/
│   │   ├── AzureEventHubConsumer.java     // Azure microservices integration
│   │   ├── CosmosDBChangeStream.java      // Change data capture from Cosmos
│   │   └── ServiceBusConnector.java       // Azure Service Bus integration
│   └── apac-api-wrapper/
│       ├── VendorAPIGateway.java          // Black-box integration for APAC
│       ├── JavaStackTelemetry.java        // Extract observability data
│       └── StandardizedEventMapper.java   // Map vendor events to standard format
├── apis/
│   ├── customer-api/
│   │   ├── CustomerQueryAPI.java          // Sub-2-second customer lookups
│   │   ├── RealtimeUpdatesAPI.java        // Streaming customer updates
│   │   └── ComplianceQueryAPI.java        // Audit and compliance queries
│   ├── operational-dashboards/
│   │   ├── OperationsDashboardAPI.java    // Real-time operational views
│   │   ├── RegionalDashboardAPI.java      // Region-specific monitoring
│   │   └── LatencyMonitoringAPI.java      // Performance monitoring
│   └── embedded-widgets/
│       ├── MarketingWidgetAPI.java        // Campaign tool integrations
│       ├── BIEmbedAPI.java               // Executive BI platform widgets
│       └── CallCenterAPI.java            // Customer service integrations
├── infrastructure/
│   ├── kafka-streams/
│   │   ├── CustomerEventProcessor.java    // Real-time event processing
│   │   ├── RegionalTopicManager.java      // Region-specific Kafka topics
│   │   └── ComplianceEventFilter.java     // Filter events by compliance rules
│   ├── observability/
│   │   ├── DistributedTracing.java        // End-to-end trace correlation
│   │   ├── MetricsCollector.java          // Cross-region metrics aggregation
│   │   └── ComplianceMonitor.java         // Regulatory compliance monitoring
│   └── deployment/
│       ├── mainframe-agents/              // Lightweight on-prem connectors
│       ├── azure-containers/              // Containerized Azure workloads
│       └── apac-adapters/                 // APAC vendor integration
├── security/
│   ├── RegionalEncryption.java            // Region-specific encryption
│   ├── CrossRegionAuth.java              // Federated authentication
│   └── ComplianceAuditLog.java           // Immutable audit logging
└── testing/
    ├── PerformanceTests.java             // Sub-2-second response validation
    ├── ScalabilityTests.java             // Concurrent user load testing
    └── ComplianceTests.java              // Regulatory validation tests
```

## Key Implementation Components

### core/customer-domain/CustomerAggregate.java

```java
/**
 * Event-sourced customer aggregate supporting progressive migration
 * Maintains single customer object across fragmented regional systems
 */
@Entity
public class CustomerAggregate {
    private CustomerId customerId;
    private List<CustomerEvent> events;
    private RegionalComplianceContext complianceContext;

    /**
     * Apply customer events while enforcing regional compliance
     * Ensures data residency and regulatory requirements
     */
    public void applyEvent(CustomerEvent event) {
        // TODO: Validate event against regional compliance rules
        // TODO: Ensure event doesn't violate data residency
        // TODO: Apply event to customer state
        // TODO: Publish to regional event stream
    }

    /**
     * Generate unified customer view from regional data sources
     * Sub-2-second response time requirement
     */
    public CustomerView generateUnifiedView() {
        // TODO: Federated query across regions
        // TODO: Merge data respecting compliance boundaries
        // TODO: Cache for performance optimization
    }
}
```

### connectors/mainframe-cdc/CobolDataExtractor.java

```java
/**
 * Change data capture from 20-year-old COBOL mainframe
 * Non-intrusive integration to avoid stability risks
 */
public class CobolDataExtractor {

    /**
     * Extract customer changes from mainframe log files
     * Supports incremental migration without big-bang cutover
     */
    public Stream<CustomerEvent> extractChanges() {
        // TODO: Parse COBOL transaction logs
        // TODO: Convert to standardized customer events
        // TODO: Handle legacy data format inconsistencies
        // TODO: Ensure minimal mainframe impact
    }

    /**
     * Batch ETL for legacy reports and reconciliation
     * Maintains existing reporting while building new capabilities
     */
    public void performBatchExtraction() {
        // TODO: Overnight batch processing
        // TODO: Data quality validation
        // TODO: Legacy system compatibility
    }
}
```

### compliance-engine/RegionalComplianceRules.java

```java
/**
 * Automated compliance enforcement for GDPR, CCPA, APAC regulations
 * Prevents manual processes that would cause business abandonment
 */
public class RegionalComplianceRules {

    /**
     * Enforce data residency requirements automatically
     * Dead-on-arrival prevention for cross-border data movement
     */
    public boolean validateDataResidency(CustomerEvent event) {
        // TODO: Check event origin and destination regions
        // TODO: Apply GDPR, CCPA, APAC residency rules
        // TODO: Block violations automatically
        // TODO: Log compliance decisions for audit
    }

    /**
     * Implement right-to-forget within days, not months
     * Automated GDPR compliance across all regional systems
     */
    public void executeRightToForget(CustomerId customerId) {
        // TODO: Coordinate deletion across all regions
        // TODO: Maintain audit trail of deletion
        // TODO: Handle legacy system limitations
    }
}
```

### apis/customer-api/CustomerQueryAPI.java

```java
/**
 * Sub-2-second customer lookup API
 * Critical performance requirement for operational adoption
 */
@RestController
public class CustomerQueryAPI {

    /**
     * Unified customer view across all regions
     * Must perform under 2 seconds to avoid adoption collapse
     */
    @GetMapping("/customer/{id}")
    public ResponseEntity<CustomerView> getCustomer(@PathVariable String id) {
        // TODO: Federated query with caching
        // TODO: Regional data aggregation
        // TODO: Compliance filtering
        // TODO: Performance monitoring
    }

    /**
     * Real-time streaming updates for customer changes
     * Marketing and analytics requirement for segmentation
     */
    @GetMapping("/customer/{id}/stream")
    public SseEmitter streamCustomerUpdates(@PathVariable String id) {
        // TODO: Event-driven updates
        // TODO: Regional event coordination
        // TODO: Compliance-filtered streaming
    }
}
```

### infrastructure/observability/DistributedTracing.java

```java
/**
 * End-to-end observability across hybrid infrastructure
 * Vendor-agnostic monitoring to avoid lock-in
 */
public class DistributedTracing {

    /**
     * Trace customer queries across mainframe, cloud, and outsourced systems
     * Critical for debugging latency and compliance issues
     */
    public void traceCustomerQuery(String customerId, String traceId) {
        // TODO: Correlate traces across regions
        // TODO: Monitor latency at each hop
        // TODO: Track compliance decision points
        // TODO: Generate vendor-agnostic metrics
    }

    /**
     * Monitor data lineage for compliance audits
     * Automated audit trail generation
     */
    public void trackDataLineage(CustomerEvent event) {
        // TODO: Record data source and transformations
        // TODO: Compliance rule applications
        // TODO: Cross-region data movement tracking
    }
}
```

## Technology Stack Details

- **Event Streaming**: Apache Kafka with regional topics for data residency
- **Change Data Capture**: Debezium for mainframe and database CDC
- **Container Orchestration**: Kubernetes with multi-cloud deployment
- **API Gateway**: Kong or Ambassador for cloud-agnostic API management
- **Event Sourcing**: EventStore or custom implementation for customer domain
- **Observability**: OpenTelemetry + Jaeger for vendor-agnostic monitoring
- **Compliance**: Custom engine with automated GDPR/CCPA/APAC enforcement
- **Caching**: Redis for sub-2-second response optimization

## Architecture Principles

1. **Regional Data Residency**: Data never leaves its region of origin
2. **Progressive Migration**: Incremental cutover without big-bang failures
3. **Cloud Agnostic**: Containerized services avoid vendor lock-in
4. **Automated Compliance**: No manual processes that cause abandonment
5. **Performance First**: Sub-2-second responses prevent adoption collapse
6. **Hybrid by Design**: Mainframe, cloud, and outsourced integration
7. **Event-Driven**: Real-time streaming with batch fallback support

## Acceptance Criteria Implementation

1. **Sub-2-Second Response**: Federated queries with aggressive caching
2. **Regulatory Compliance**: Automated enforcement prevents fines
3. **Developer Velocity**: Unified customer object eliminates data stitching
4. **No New Silos**: Federated architecture prevents duplication
5. **Operational Usability**: Real-time dashboards for front-line staff
6. **Governance Balance**: Automated compliance without rigid shadow IT triggers

This scaffold implements an event-driven data fabric that abstracts regional fragmentation while enforcing compliance automatically, supporting the complex enterprise requirements for unified customer-360 capabilities.
