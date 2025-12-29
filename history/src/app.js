// Define global variables to store data
let historyData = [];
let svgElement;
let timelineData = [];

// Load data from math.json
async function loadData() {
  try {
    const response = await fetch('physics.json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error loading math history data:', error);
    return [];
  }
}

// Download SVG file
function downloadSVG() {
  const svgData = new XMLSerializer().serializeToString(svgElement);
  const svgBlob = new Blob([svgData], {type: 'image/svg+xml'});
  const svgUrl = URL.createObjectURL(svgBlob);

  const downloadLink = document.createElement('a');
  downloadLink.href = svgUrl;
  downloadLink.download = 'math-history-timeline.svg';
  document.body.appendChild(downloadLink);
  downloadLink.click();
  document.body.removeChild(downloadLink);
}


// Show event details
function showEventDetails(event) {
  let details = `Event: ${event.key || 'N/A'}\n`;
  details += `Time: ${event.time.join(' - ')}\n`;
  if (event.data.persons) {
    details += `People: ${Array.isArray(event.data.persons) ? event.data.persons.join(', ') : event.data.persons}\n`;
  }
  if (event.data.paper) {
    details += `Reference: ${event.data.paper}\n`;
  }
  alert(details);
}

// Set up event listeners
function setupEventListeners() {
  // Download SVG button
  document.getElementById('download-btn').addEventListener('click', downloadSVG);

  // Zoom functionality
  let scale = 1;
  document.getElementById('zoom-in').addEventListener('click', () => {
    scale = Math.min(scale * 1.2, 3);
    svgElement.style.transform = `scale(${scale})`;
  });

  document.getElementById('zoom-out').addEventListener('click', () => {
    scale = Math.max(scale / 1.2, 0.5);
    svgElement.style.transform = `scale(${scale})`;
  });
}

// Initialize page
document.addEventListener('DOMContentLoaded', async function() {
  // 加载数据
  historyData = await loadData();

  // 按时间排序
  historyData.sort((a, b) => parseInt(a.time[0]) - parseInt(b.time[0]));

  // 初始化SVG
  svgElement = document.getElementById('timeline-svg');
  
  // Add defs element for gradients
  const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
  svgElement.appendChild(defs);

  // Render timeline
  renderTimeline();

  // Set up event listeners
  setupEventListeners();
});
