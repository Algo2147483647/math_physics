
// Truncate text to fit space
function truncateText(text, maxLength) {
  if (!text) return '';
  text = text.toString();
  return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
}

// Function to generate random soft colors
function getRandomColor() {
  // Generate soft colors with limited hue range for better visual appearance
  const hue = Math.floor(Math.random() * 360);
  const saturation = 30 + Math.floor(Math.random() * 50); // 30-80% saturation for softness
  const lightness = 70 + Math.floor(Math.random() * 20); // 70-90% lightness for softness

  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
}

// Function to generate soft colors for timeline ranges
function getSoftColor() {
  // Generate soft pastel colors with more consistency
  const hue = Math.floor(Math.random() * 360);
  const saturation = 20 + Math.floor(Math.random() * 30); // Lower saturation for softer look
  const lightness = 80 + Math.floor(Math.random() * 15); // Higher lightness for softer look

  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
}
