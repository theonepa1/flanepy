interface PyWebViewAPI {
  health_check(): Promise<{ status: string }>;
  hello(): Promise<{ message: string } | { error: string }>;
  echo(message: string): Promise<{ message: string; delay: number } | { error: string }>;
}

interface Window {
  pywebview?: {
    api?: PyWebViewAPI;
  };
} 