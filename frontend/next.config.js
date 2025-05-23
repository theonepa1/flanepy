/** @type {import('next').NextConfig} */
const nextConfig = {
  // Only enable static exports in production
  output: process.env.NODE_ENV === 'production' ? 'export' : undefined,
  images: {
    unoptimized: true,  // Required for static export
  },
  // Disable server-side features in production
  trailingSlash: process.env.NODE_ENV === 'production',
  // Enable development mode
  webpack: (config, { dev, isServer }) => {
    // Enable hot reloading in development
    if (dev && !isServer) {
      config.watchOptions = {
        poll: 1000, // Check for changes every second
        aggregateTimeout: 300, // Delay before rebuilding
      }
    }
    return config
  },
  // Development server configuration
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://localhost:5000/api/:path*',
      },
    ];
  },
}

module.exports = nextConfig 