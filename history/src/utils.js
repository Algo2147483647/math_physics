
// Truncate text to fit space
function truncateText(text, maxLength) {
  if (!text) return '';
  text = text.toString();
  return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
}


// Track which colors have been used
let usedColors = [];

// Function to generate random soft colors
function getRandomColor() {
  // All common colors have been used, generate a random soft pastel color
  const hue = Math.floor(Math.random() * 360);
  const saturation = 20 + Math.floor(Math.random() * 50);
  const lightness = 80 + Math.floor(Math.random() * 20);

  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
}
