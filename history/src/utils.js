
// Truncate text to fit space
function truncateText(text, maxLength) {
  if (!text) return '';
  text = text.toString();
  return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
}

// Function to generate random soft colors
function getRandomColor() {
  // Generate soft pastel colors with more consistency
  // Using a more limited hue range for better visual harmony
  const hue = Math.floor(Math.random() * 360); // Blues, purples, pinks, greens
  const saturation = 20 + Math.floor(Math.random() * 50); // Lower saturation for softer look
  const lightness = 80 + Math.floor(Math.random() * 20); // Higher lightness for softer look

  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
}
