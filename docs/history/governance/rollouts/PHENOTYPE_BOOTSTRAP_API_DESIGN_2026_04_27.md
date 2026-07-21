# phenotype-bootstrap crate API design (Kimi-generated 2026-04-27)

>>> dispatch-worker tier=nvidia/moonshotai/kimi-k2.5 model=nvidia/moonshotai/kimi-k2.5 endpoint=http://localhost:20128/v1
>>> routed to backend: moonshotai/kimi-k2.5
 ```rust
// Config (figment wrapper)
pub struct ConfigLoader;
impl ConfigLoader {
    pub fn new() -> Self;
    pub fn with_prefix(self, prefix: &str) -> Self;
    pub fn with_file(self, path: &str) -> Self;
    pub fn load<T: serde::de::DeserializeOwned>(self) -> Result<T, figment::Error>;
}

// Telemetry (OpenTelemetry + tracing_subscriber)
pub struct TelemetryConfig { 
    pub service_name: String, 
    pub otlp_endpoint: Option<String>, 
    pub log_level: tracing::Level 
}
pub struct TelemetryGuard;
impl TelemetryGuard {
    pub fn init(cfg: TelemetryConfig) -> Result<Self, TelemetryError>;
    pub async fn shutdown(self);
}
pub enum TelemetryError { SetupFailed(String), ExporterError(opentelemetry::trace::TraceError) }

// Panic hooks
pub fn install_panic_hook();

// Graceful shutdown (tokio signal handling)
pub async fn shutdown_signal() -> ShutdownReason;
pub enum ShutdownReason { Terminated, Interrupted }
```
