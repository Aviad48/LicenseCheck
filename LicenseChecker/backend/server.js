const express = require('express');
const app = express();
const PORT = 3000;

// Mock data
const licenseData = {
  isExpired: false,
  licenseKey: 'ABC-123-XYZ',
  usageCount: 42,
};

// Routes
app.get('/api/isLicenseExpired', (req, res) => {
  res.json({ message: licenseData.isExpired ? 'License is expired' : 'License is active' });
});

app.get('/api/checkLicense', (req, res) => {
  res.json({ message: `License Key: ${licenseData.licenseKey}` });
});

app.get('/api/checkUsageCount', (req, res) => {
  res.json({ count: licenseData.usageCount });
});

// Start server
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
