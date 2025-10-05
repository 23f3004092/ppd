<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Hello — My GitHub Pages</title>

  <!-- Simple pleasant styling -->
  <style>
    :root{
      --bg: #0f1724;
      --card: #0b1220;
      --accent: #7dd3fc;
      --muted: #94a3b8;
    }
    html,body{
      height:100%;
      margin:0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background: linear-gradient(180deg,#071022 0%, var(--bg) 100%);
      color: #e6edf3;
      -webkit-font-smoothing:antialiased;
      -moz-osx-font-smoothing:grayscale;
    }
    .wrap{
      min-height:100%;
      display:flex;
      align-items:center;
      justify-content:center;
      padding:48px 20px;
      box-sizing:border-box;
    }
    .card{
      background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));
      border:1px solid rgba(255,255,255,0.04);
      padding:36px;
      border-radius:16px;
      max-width:820px;
      width:100%;
      box-shadow: 0 8px 30px rgba(2,6,23,0.6);
      text-align:center;
    }
    h1{
      margin:0 0 8px 0;
      font-size: clamp(28px, 4vw, 48px);
      line-height:1.05;
      letter-spacing: -0.02em;
    }
    p.lead{
      margin:0 0 18px 0;
      color:var(--muted);
      font-size: clamp(14px, 1.6vw, 18px);
    }
    .btn{
      display:inline-block;
      margin-top:12px;
      padding:10px 18px;
      border-radius:10px;
      text-decoration:none;
      font-weight:600;
      border:1px solid rgba(125,211,252,0.12);
      background: linear-gradient(90deg, rgba(125,211,252,0.12), rgba(125,211,252,0.08));
      color:var(--accent);
      transition:transform .12s ease, box-shadow .12s ease;
    }
    .btn:hover{ transform: translateY(-3px); box-shadow: 0 8px 20px rgba(13,42,65,0.45); }
    footer{
      margin-top:18px;
      color:var(--muted);
      font-size:13px;
    }
    code.inline {
      background: rgba(255,255,255,0.03);
      padding:4px 8px;
      border-radius:6px;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, "Roboto Mono", monospace;
      font-size:13px;
      color:#cfeffd;
    }
  </style>
</head>
<body>
  <div class="wrap">
    <main class="card" role="main" aria-live="polite">
      <h1>Hello 👋</h1>
      <p class="lead">This is a minimal `index.html` ready for GitHub Pages — simple, responsive, and friendly.</p>

      <a class="btn" href="https://github.com/" target="_blank" rel="noopener noreferrer">Visit GitHub</a>

      <footer>
        Deployed with GitHub Pages — place this file at the repository root or the `gh-pages` branch.<br>
        Tip: rename this file to <code class="inline">index.html</code> (if it isn't) and push to your repo.
      </footer>
    </main>
  </div>
</body>
</html>
