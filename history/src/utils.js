// Truncate text to fit space
function truncateText(text, maxLength) {
  if (!text) return '';
  text = text.toString();
  return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
}


// Track which colors have been used
let usedColors = [];

// Function to generate random soft colors
function getRandomColor(x, width) {
  // Calculate hue based on x position to ensure similar colors for nearby x values
  const baseHue = (x * 10) % 360; // Use golden angle to ensure good color distribution
  
  // Calculate saturation based on width - smaller width means higher saturation
  // Using a range of 30-100% for saturation, with smaller widths being more saturated
  const saturation = Math.max(30, 100 - (width * 10)); // Adjust multiplier as needed
  
  // Keep lightness in a soft range to maintain the soft color preference
  const lightness = 70 + Math.floor(Math.random() * 10); // Soft lightness between 70-80%
  
  return `hsl(${baseHue}, ${saturation}%, ${lightness}%)`;
}