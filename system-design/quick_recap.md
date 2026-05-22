# System Design Book

A structured set of notes for learning system design from fundamentals to real-world architecture.

## How To Use This Book

1. Start with the fundamentals to build shared vocabulary.
2. Move through architecture, scalability, storage, and performance.
3. Use the security and reliability chapters as design checklists.
4. Practice with the blueprint and case-study prompts at the end.

## Table Of Contents

1. Foundations
2. Web And Communication
3. Architectural Patterns
4. Scalability
5. Storage And Databases
6. Performance And Caching
7. Reliability And Availability
8. Security
9. System Design Blueprint
10. Case Studies

---

# Part I: Foundations

## 1. OSI Model

The OSI (Open Systems Interconnection) model is a 7-layer conceptual model that standardizes how data moves across a network.

### The 7 Layers

1. Application - HTTP, APIs, user-facing protocols
2. Presentation - encryption, compression, data format
3. Session - session management
4. Transport - TCP, UDP, ports
5. Network - IP, routing
6. Data Link - MAC addresses, switches
7. Physical - cables, signals, voltages

### Practical View

- Application, Presentation, Session -> application layer concerns
- Transport -> transport layer concerns
- Network -> internet layer concerns
- Data Link and Physical -> network access concerns

### Flow

- Sender: 7 -> 1
- Receiver: 1 -> 7

## 2. Core Web Basics

### Proxy And Network Utilities

- Forward proxy: sits between client and the internet
- Reverse proxy: sits between the internet and backend servers
- DNS: translates domain names to IP addresses
- API gateway: single entry point to microservices; handles routing, auth, rate limiting, monitoring, and response aggregation
- CDN: geographically distributed edge servers that cache and serve content closer to users

### Why CDNs Matter

- Reduce latency
- Reduce origin load
- Improve global performance
- Useful for media-heavy or globally distributed products

## 3. Protocols

### TCP And UDP

Both TCP and UDP sit at the transport layer and move data between applications on different machines.

- TCP: reliable, connection-oriented, ordered delivery, retransmission, congestion control
- UDP: faster, connectionless, no delivery guarantees

### HTTP And TCP

- HTTP defines what is sent
- TCP defines how it is reliably delivered

Flow:

Client -> TCP handshake -> HTTP request -> TCP transport -> HTTP response

### HTTP

- Application-layer protocol for transferring web resources
- Works over port 80
- Stateless
- Common methods: GET, POST, PUT, DELETE, PATCH

### HTTP Status Codes

- 1xx: informational
- 2xx: success
  - 200: OK
  - 201: Created
- 3xx: redirection
  - 304: Not Modified
- 4xx: client errors
- 5xx: server errors

### HTTPS

- Secure version of HTTP
- Works over port 443
- Uses TLS for encryption and integrity

### Statelessness And State Handling

HTTP does not remember previous requests. State is usually handled with:

- Cookies
- Sessions
- Tokens

## 4. API Styles

### REST

REST is an architectural style for stateless APIs where resources are manipulated using HTTP methods.

#### REST Constraints

- Client-server architecture
- Statelessness
- Cacheability
- Layered system
- Uniform interface

### JSON Vs XML

- JSON: lightweight, readable, faster to parse
- XML: verbose, useful for legacy systems and strict schema validation

### Real-Time Communication

Traditional HTTP is request-response only, so real-time updates need other approaches.

#### Polling

- Client repeatedly asks server for updates

#### Long Polling

- Client sends request
- Server waits until data is available
- Server responds when it has data

#### WebSockets

- Persistent full-duplex communication
- Starts with an HTTP upgrade handshake
- Used for chat, multiplayer games, collaborative apps

#### Server-Sent Events

- Server pushes updates to the client over a persistent HTTP connection
- Useful for notifications and live feeds

### Modern API Protocols

#### gRPC

- High-performance RPC framework from Google
- Uses protobuf instead of JSON
- Best for low-latency service-to-service communication
- Less suitable for browser-heavy public APIs

#### GraphQL

- Client requests exactly the data it needs
- Solves overfetching and underfetching
- Flow: client query -> schema -> resolver -> database -> response

---

# Part II: Architectural Patterns

## 5. Architecture Thinking

Architectural patterns describe how components in a system relate to one another.

### Main Considerations

- Performance: responsiveness under load
- Maintainability: ease of updates and changes
- Scalability: ability to handle growth in traffic or data

## 6. Monolith

A monolithic architecture is a single unified application where business logic, API handling, and data access are deployed together.

### Pros

- Simple
- Easier for small applications
- Easy to deploy initially

### Cons

- Hard to scale
- Hard to maintain at large size
- One failure can affect the whole system

## 7. Layered Architecture

Layered architecture splits the app into layers, and each layer talks mainly to adjacent layers.

### Common Layers

- Controller layer: handles requests
- Service layer: business logic
- Repository layer: database access

### Deployment Shapes

- 2-tier: client -> database
- 3-tier: presentation -> application -> data
- N-tier: frontend -> gateway -> services -> data

### Pros

- Separation of concerns
- Easier to scale than a monolith

### Cons

- Layer coupling
- Extra latency from layered calls

## 8. Microservices

Microservices are small, independent services focused on specific business capabilities.

### Pros

- Independent scaling
- Flexible technology choices
- Better fault isolation

### Cons

- More DevOps complexity
- Distributed system complexity

## 9. Event-Driven Architecture

In event-driven systems, services communicate by producing and consuming events instead of directly calling each other.

### Example Flow

User -> Order Service -> OrderPlaced event -> Event Broker -> Payment / Inventory / Email services

### Brokers

- Queue-based brokers: point-to-point, one consumer processes a message
- Broadcast brokers: multiple consumers receive the same event

### Common Challenges

- Eventual consistency
- Ordering guarantees
- Debugging distributed flows

---

# Part III: Scalability

## 10. What Scalability Means

Scalability is the ability of a system to handle increasing load while maintaining performance, availability, and reliability.

### Why Systems Need To Scale

- User growth
- Data growth
- Peak traffic events

### Common Challenges

- Latency
- Bottlenecks
- Memory limits
- Single-threaded processing
- Downtime
- Cost

## 11. Scaling Strategies

### Vertical Scaling

- Add more CPU, RAM, or disk to the same server
- Simple to implement
- Limited by hardware
- Can become a single point of failure

### Horizontal Scaling

- Add more servers and distribute the load
- Needs load balancers and stateless design
- More resilient, but more complex

### Diagonal Scaling

- Hybrid approach
- Start vertically, then add horizontal scale as needed
- Often a practical long-term strategy

## 12. Load Balancers

A load balancer distributes traffic across multiple servers so no single server gets overloaded.

### Benefits

- High availability
- Traffic distribution
- Failure handling
- Better performance

### Types By Layer

- Layer 4: routes using IP and TCP/UDP port data
- Layer 7: routes using HTTP content such as headers, cookies, params, and paths

### Types By Deployment

- Hardware
- Software
- Cloud-based

### Strategies

#### Static

- Round robin
- Least connections
- IP hashing

#### Dynamic

- Least response time
- Adaptive load balancing
- Weighted load balancing

## 13. Autoscaling

Autoscaling automatically adjusts compute resources based on demand.

### Triggers

- CPU
- Memory
- Request rate
- Queue length

### Policies

- Reactive: scale after thresholds are crossed
- Predictive: scale based on trends

### Cost Optimization

- Avoid over-provisioning
- Use spot or preemptible instances for fault-tolerant jobs
- Apply quotas and limits
- Use scale-to-zero where possible
- Rightsize resources

---

# Part IV: Storage And Databases

## 14. Data Types And Storage Forms

### Structured Vs Unstructured Data

- Structured: rows, columns, predefined schema
- Unstructured: no fixed schema, such as images, videos, logs

### Storage Categories

- Database storage
- Object storage
- File storage
- Block storage

## 15. ACID And CAP

### ACID

- Atomicity: all or nothing
- Consistency: each read returns valid data
- Isolation: transactions do not interfere
- Durability: committed changes persist

### CAP Theorem

In distributed systems, when a partition happens, a system must trade off between consistency and availability.

- Consistency: every read gets the latest write
- Availability: every request gets a response
- Partition tolerance: system keeps operating despite network failures

### Common Tradeoffs

- CP: correctness over availability
- AP: availability over strict freshness
- CA: only realistic in non-distributed systems

## 16. SQL And NoSQL

### Relational Databases

- Strict schema
- Joins
- ACID properties

### Limitations

- Not ideal for schema-less data
- Harder to scale horizontally
- Less natural for document-like data

### NoSQL Types

- Document: flexible JSON-like documents
- Key-value: very fast reads and writes
- Graph: nodes and edges for relationships
- Columnar: stores data by columns

### Polyglot Persistence

Use different databases for different needs in the same system.

Examples:

- Orders -> SQL
- Catalog -> Document DB
- Search -> Elasticsearch
- Reports -> Data warehouse

## 17. Scaling Databases

### Vertical Scaling

- Increase resources on a single database server
- Simpler architecture
- Strong consistency
- Hardware limits and single-point-of-failure risk

### Horizontal Scaling

- Add more database nodes
- Better elasticity and fault tolerance
- More complex architecture
- May introduce weaker consistency

### Eventual Consistency

Data across nodes eventually converges, but not immediately after a write.

## 18. Replication

Replication copies data from one database node to another for redundancy and performance.

### Benefits

- Fault tolerance
- Better read performance
- Higher availability

### Patterns

- Leader-follower replication
- Read replicas

### Tradeoff

Replicas may lag behind the primary, which can create stale reads.

## 19. Sharding

Sharding splits data across multiple database nodes.

### Types

- Horizontal sharding: rows are distributed across shards
- Vertical sharding: tables or columns are split across databases

### Strategies

- Range-based: split by key ranges
- Hash-based: distribute by hash; often paired with consistent hashing
- Geo-based: shard by region

### Why It Matters

- Helps when a single node cannot handle read, write, or storage volume

## 20. Object Storage

Object storage stores data as objects rather than files or blocks.

### Object Components

- Data
- Metadata
- Unique identifier

### Bucket

A logical container for objects.

### Use Cases

- Images
- Videos
- Audio
- Emails
- Logs

### Examples

- Amazon S3
- Google Cloud Storage
- Azure Blob Storage

---

# Part V: Performance

## 21. Performance Goals

System performance means efficiency under load.

### Metrics

- Latency: time per request
- Throughput: requests per second
- Efficiency: CPU and memory usage

### Goal

Low latency and high throughput

## 22. SLA, SLO, And SLI

- SLA: external contract
- SLO: internal target
- SLI: actual measurement

## 23. Load Testing

- Load test: normal traffic
- Stress test: break point
- Spike test: sudden surge
- Endurance test: long-running load

## 24. Monitoring And Observability

### Monitor

- Latency p50, p95, p99
- Throughput
- Error rate
- CPU and memory
- Database queries

### Observe

- Metrics
- Logs
- Traces

## 25. Caching

Caching stores frequently accessed data so it can be retrieved faster than recomputation or repeated database/API calls.

### Benefits

- Lower latency
- Less backend load
- Better scalability

### Types

- Client-side caching
- Server-side caching
- CDN caching
- Database or query caching

### Strategies

- Write-through
- Write-back
- Cache-aside
- Explicit caching

### Eviction Policies

- LRU
- LFU
- FIFO
- TTL

## 26. Redis

Redis is an in-memory key-value store for fast reads and writes.

### Key Characteristics

- Very low latency
- TTL support
- Pub/Sub
- Persistence options
- Rich data structures

### Use Cases

- Caching
- Session storage
- Rate limiting
- Real-time counters
- Messaging

---

# Part VI: Reliability And Availability

## 27. Reliability Basics

Reliability is the ability of a system to function correctly over time, even when components fail.

## 28. High Availability

High availability means the system remains accessible with minimal downtime.

## 29. Fault Tolerance

Fault tolerance is the ability to keep working even when parts of the system fail.

## 30. Failover

Failover switches traffic or work to a healthy component when the primary one fails.

## 31. Backup And Recovery

Backups protect data so it can be restored after loss, corruption, or disaster.

## 32. Disaster Recovery

Disaster recovery is the plan for restoring services after a major outage or catastrophic failure.

---

# Part VII: Security

## 33. Security Basics

Security protects systems, data, and users.

### Goals

- Trust
- Data protection
- System reliability

## 34. CIA Triad

1. Confidentiality - prevent unauthorized access
2. Integrity - prevent tampering
3. Availability - keep the system up

## 35. Authentication And Authorization

- Authentication: who are you?
- Authorization: what can you access?

## 36. Threat Modeling

Threat modeling identifies attackers, goals, and attack paths.

Flow:

assets -> attack surface -> threats -> mitigation

## 37. Attack Surface

Common entry points:

- APIs
- Login forms
- Ports
- Uploads

## 38. Common Attack Vectors

- Insecure APIs
- Misconfigured servers
- Weak auth
- Open ports

## 39. Common Attacks

### DDoS

- Floods the system
- Threatens availability
- Mitigation: rate limits, CDN, autoscaling

### MITM

- Intercepts communication
- Mitigation: HTTPS, TLS, VPN

### Injection

- Malicious input alters behavior
- Mitigation: validation, parameterized queries

### Spoofing

- Impersonation
- Mitigation: MFA, token validation, whitelisting

### XSS

- Injects malicious JavaScript into trusted pages
- Mitigation: sanitize input, CSP

### CSRF

- Forces unwanted actions on behalf of a logged-in user
- Mitigation: CSRF tokens

## 40. STRIDE

- S: Spoofing
- T: Tampering
- R: Repudiation
- I: Information disclosure
- D: Denial of service
- E: Elevation of privilege

## 41. Authentication

### Username And Password

- Use HTTPS
- Store passwords as hashes, not plain text

### OAuth 2.0

- Delegated authorization protocol
- Lets apps access user data without sharing the password

### OpenID Connect

- Built on OAuth 2.0
- Adds identity information
- Used for SSO

### JWT

- Token format: header.payload.signature
- Stateless and scalable
- Harder to revoke
- Must be handled securely with expiry and safe storage

## 42. Session Vs Token

### Session-Based Auth

- Server stores session data
- Client stores session ID in a cookie
- Easy to revoke
- Needs shared storage to scale

### Token-Based Auth

- Server signs a token
- Client sends token in requests
- Stateless and scalable
- Hard logout is harder

## 43. Session Security

### Risks

- XSS stealing cookies
- No HTTPS sniffing
- Session fixation

### Protections

- HttpOnly
- Secure
- SameSite
- Rotate session IDs
- Expire and renew sessions

## 44. CORS

CORS is a browser-enforced policy that controls whether a frontend origin can read responses from a backend origin.

### Key Idea

- Origin = protocol + domain + port

### Flow

- Browser sends Origin header
- Server responds with Access-Control-Allow-Origin

### Requests

- Simple request
- Preflight request using OPTIONS

### Risk

Misconfigured CORS can expose APIs to malicious sites.

## 45. Best Practices

- Least privilege
- Validate inputs
- Use HTTPS
- Secure defaults
- Defense in depth

---

# Part VIII: System Design Blueprint

## 46. Design Process

### Step 1: Understand The Problem

- Functional requirements
- Non-functional requirements
- Constraints: time, budget, regulatory, technical

### Step 2: Estimate Scale

- Peak load
- Traffic pattern
- User growth
- Storage, bandwidth, and compute needs

### Step 3: High-Level Design

- Core services
- Public APIs
- Sync vs async communication
- Service interactions

### Step 4: Make Tech And Infra Decisions

- SQL vs NoSQL
- Caching
- Load balancing
- Autoscaling
- Replication
- Cost vs performance tradeoffs

## 47. Interview Checklist

- Clarify requirements
- Estimate scale
- Identify bottlenecks
- Propose architecture
- Explain data model
- Handle failure scenarios
- Cover security
- Discuss tradeoffs
- Mention observability and operations

---

# Part IX: Case Studies

The example files in the source folder are currently mostly empty, so this section turns them into a practical practice list.

## 48. TinyURL

Focus areas:

- URL generation
- Hashing and collision handling
- Redirect path performance
- Analytics

## 49. BookMyShow

Focus areas:

- Seat reservation
- Concurrency control
- Search
- Payments

## 50. Instagram

Focus areas:

- Feed generation
- Media storage
- Caching
- Notifications

## 51. Notifications

Focus areas:

- Event ingestion
- Fanout
- Delivery channels
- Retry and deduplication

## 52. WhatsApp

Focus areas:

- Real-time messaging
- Presence
- Delivery receipts
- End-to-end security

## 53. eBay

Focus areas:

- Listings
- Search
- Bidding
- Transaction consistency

## 54. Airbnb

Focus areas:

- Search and filters
- Availability calendars
- Booking flow
- Pricing

## 55. Google Drive

Focus areas:

- File storage
- Sync
- Sharing permissions
- Versioning

## 56. YouTube

Focus areas:

- Upload pipeline
- Transcoding
- Streaming delivery
- Recommendations

## 57. Google

Focus areas:

- Distributed search
- Indexing
- Ranking
- Scale and latency

## 58. Amazon

Focus areas:

- Catalog
- Cart
- Orders
- Inventory
- Recommendations

## 59. Uber

Focus areas:

- Real-time location tracking
- Matching
- ETA calculation
- Surge pricing

---

# Appendix: Quick Reference

## Web And Networking

- HTTP: application-layer request/response protocol
- HTTPS: HTTP over TLS
- TCP: reliable transport
- UDP: fast, connectionless transport
- REST: stateless resource-based API style
- WebSockets: persistent two-way communication
- SSE: server push over HTTP

## Scaling

- Vertical scaling: bigger machine
- Horizontal scaling: more machines
- Diagonal scaling: hybrid approach

## Data

- SQL: structured, relational, strong consistency
- NoSQL: flexible schema, scale-oriented
- Replication: copies data
- Sharding: splits data
- Object storage: stores blobs as objects

## Performance

- Latency: time to respond
- Throughput: work per second
- Cache: store hot data closer to access

## Security

- AuthN: identity
- AuthZ: permissions
- CIA: confidentiality, integrity, availability

