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

// Create and show event card
function showEventCard(event, x, y) {
  const eventCard = document.getElementById('event-card');
  
  // Create content for the card
  let content = `<h3>${event.key || 'N/A'}</h3>`;
  
  // Add year (time)
  content += `<div class="event-year">${event.time.join(' ~ ')}</div>`;
  
  // Add space (location)
  if (event.space && event.space.length > 0) {
    content += `<div class="event-space">${event.space.join(', ')}</div>`;
  }
  
  // Add data fields
  if (event.data) {
    content += '<div class="event-data">';
    for (const [key, value] of Object.entries(event.data)) {
      if (Array.isArray(value)) {
        content += `<div><strong>${key}:</strong> ${value.join(', ')}</div>`;
      } else {
        content += `<div><strong>${key}:</strong> ${value}</div>`;
      }
    }
    content += '</div>';
  }
  
  eventCard.innerHTML = content;
  eventCard.style.display = 'block';
  
  // Store mouse coordinates for scroll updates
  eventCard.setAttribute('data-mouse-x', x);
  eventCard.setAttribute('data-mouse-y', y);
  
  // Position the card near the mouse, making sure it stays within the viewport
  const cardWidth = eventCard.offsetWidth;
  const cardHeight = eventCard.offsetHeight;
  
  // Adjust position to prevent card from going off-screen
  let adjustedX = x + 10;
  let adjustedY = y + 10;
  
  // Check if card would go off right edge
  if (adjustedX + cardWidth > window.innerWidth) {
    adjustedX = x - cardWidth - 10;
  }
  
  // Check if card would go off bottom edge
  if (adjustedY + cardHeight > window.innerHeight) {
    adjustedY = y - cardHeight - 10;
  }
  
  // Ensure card doesn't go off left or top edge
  if (adjustedX < 0) {
    adjustedX = 0;
  }
  
  if (adjustedY < 0) {
    adjustedY = 0;
  }
  
  eventCard.style.left = adjustedX + 'px';
  eventCard.style.top = adjustedY + 'px';
}

// Hide event card
function hideEventCard() {
  const eventCard = document.getElementById('event-card');
  eventCard.style.display = 'none';
  eventCard.removeAttribute('data-mouse-x');
  eventCard.removeAttribute('data-mouse-y');
}

// Update event card position when scrolling
function updateEventCardPosition(x, y) {
  const eventCard = document.getElementById('event-card');
  if (eventCard.style.display !== 'none') {
    // Store mouse coordinates for scroll updates
    eventCard.setAttribute('data-mouse-x', x);
    eventCard.setAttribute('data-mouse-y', y);
    
    // Position the card near the mouse, making sure it stays within the viewport
    const cardWidth = eventCard.offsetWidth;
    const cardHeight = eventCard.offsetHeight;
    
    // Adjust position to prevent card from going off-screen
    let adjustedX = x + 10;
    let adjustedY = y + 10;
    
    // Check if card would go off right edge
    if (adjustedX + cardWidth > window.innerWidth) {
      adjustedX = x - cardWidth - 10;
    }
    
    // Check if card would go off bottom edge
    if (adjustedY + cardHeight > window.innerHeight) {
      adjustedY = y - cardHeight - 10;
    }
    
    // Ensure card doesn't go off left or top edge
    if (adjustedX < 0) {
      adjustedX = 0;
    }
    
    if (adjustedY < 0) {
      adjustedY = 0;
    }
    
    eventCard.style.left = adjustedX + 'px';
    eventCard.style.top = adjustedY + 'px';
  }
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
  
  // Add scroll event listener to update card position
  window.addEventListener('scroll', updateCardPositionOnScroll, { passive: true });
  window.addEventListener('resize', updateCardPositionOnScroll, { passive: true });
}

// Function to update card position when scrolling occurs
function updateCardPositionOnScroll() {
  const eventCard = document.getElementById('event-card');
  if (eventCard.style.display !== 'none') {
    // Re-position the card using stored mouse coordinates
    const storedMouseX = eventCard.getAttribute('data-mouse-x');
    const storedMouseY = eventCard.getAttribute('data-mouse-y');
    
    if (storedMouseX && storedMouseY) {
      updateEventCardPosition(parseInt(storedMouseX), parseInt(storedMouseY));
    }
  }
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
