
// Truncate text to fit space
function truncateText(text, maxLength) {
  if (!text) return '';
  text = text.toString();
  return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
}

// Predefined common colors that are visually distinct
const commonColors = [
  // Red variations
  "hsl(0, 80%, 85%)", "hsl(0, 60%, 80%)", "hsl(0, 40%, 85%)",
  // Orange variations
  "hsl(30, 80%, 85%)", "hsl(30, 60%, 80%)",
  // Yellow variations
  "hsl(60, 80%, 85%)", "hsl(60, 60%, 80%)", "hsl(60, 40%, 85%)",
  // Green variations
  "hsl(120, 80%, 85%)", "hsl(120, 60%, 80%)", "hsl(120, 40%, 85%)", "hsl(100, 70%, 82%)", "hsl(140, 65%, 83%)",
  // Cyan variations
  "hsl(180, 80%, 85%)", "hsl(180, 60%, 80%)", "hsl(180, 40%, 85%)",
  // Blue variations
  "hsl(240, 80%, 85%)", "hsl(240, 60%, 80%)", "hsl(240, 40%, 85%)", "hsl(200, 70%, 82%)", "hsl(260, 65%, 83%)",
  // Purple variations
  "hsl(270, 80%, 85%)", "hsl(270, 60%, 80%)", "hsl(270, 40%, 85%)",
  // Magenta variations
  "hsl(300, 80%, 85%)", "hsl(300, 60%, 80%)", "hsl(300, 40%, 85%)",
  // Pink variations
  "hsl(330, 80%, 85%)", "hsl(330, 60%, 80%)",
  // Brown variations
  "hsl(30, 40%, 75%)", "hsl(20, 50%, 70%)", "hsl(15, 60%, 65%)",
  // Gray variations
  "hsl(0, 0%, 85%)", "hsl(0, 0%, 75%)", "hsl(0, 0%, 65%)", "hsl(0, 0%, 90%)", "hsl(0, 0%, 80%)",
  // Soft pastel colors
  "hsl(30, 30%, 85%)", "hsl(90, 35%, 85%)", "hsl(150, 40%, 85%)", "hsl(210, 35%, 85%)",
  "hsl(270, 30%, 85%)", "hsl(330, 35%, 85%)", "hsl(45, 40%, 85%)", "hsl(75, 35%, 85%)",
  "hsl(105, 30%, 85%)", "hsl(135, 35%, 85%)", "hsl(165, 40%, 85%)", "hsl(195, 35%, 85%)",
  "hsl(225, 30%, 85%)", "hsl(255, 35%, 85%)", "hsl(285, 40%, 85%)", "hsl(315, 35%, 85%)",
  "hsl(345, 30%, 85%)", "hsl(15, 35%, 85%)"
];

// Track which colors have been used
let usedColors = [];

// Function to generate random soft colors
function getRandomColor() {
  // If we haven't used all common colors yet, use one from the list
  if (usedColors.length < commonColors.length) {
    // Get a random color from the remaining common colors
    let availableColors = commonColors.filter(color => !usedColors.includes(color));
    let randomIndex = Math.floor(Math.random() * availableColors.length);
    let selectedColor = availableColors[randomIndex];
    
    // Add to used colors list
    usedColors.push(selectedColor);
    
    return selectedColor;
  } else {
    // All common colors have been used, generate a random soft pastel color
    const hue = Math.floor(Math.random() * 360);
    const saturation = 20 + Math.floor(Math.random() * 50);
    const lightness = 80 + Math.floor(Math.random() * 20);
    
    return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
  }
}
