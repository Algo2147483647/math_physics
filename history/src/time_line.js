
// Render SVG timeline
function renderTimeline() {
  // Clear SVG
  clearSVG();

  // Calculate dimensions
  const { minYear, maxYear, width, height, margin, innerWidth, innerHeight } = calculateDimensions();

  // Calculate year-to-position mapping
  const yearScale = createYearScale(minYear, maxYear, margin, innerHeight);

  // Draw vertical timeline
  drawVerticalTimeline(height, margin);

  // Add year ticks
  addYearTicks(minYear, maxYear, yearScale, margin, height);

  // Process events
  timelineData = processEvents(yearScale);

  // 对所有事件 timelineData 的父子关系进行对齐，缺少的话补充上去，即保证每个节点的parent和kids都是对的，不缺少的
  alignParentChildRelationships();

  // Separate time ranges and single points
  const { timeRanges, singlePoints } = separateEvents(timelineData);

  // Calculate horizontal positions for time ranges and single points to avoid conflicts
  calculateHorizontalPositions(timeRanges, singlePoints, margin);

  // Draw time ranges first
  drawTimeRanges(timeRanges, margin, height, yearScale);

  // Draw single points separately
  drawSinglePoints(singlePoints, margin, height);
}

// 对所有事件 timelineData 的父子关系进行对齐，缺少的话补充上去，即保证每个节点的parent和kids都是对的，不缺少的
function alignParentChildRelationships() {
  // 首先，清空所有事件的 kids 数组
  timelineData.forEach(event => {
    if (!event.kids) {
      event.kids = [];
    }
  });

  // 遍历所有事件，建立正确的父子关系
  timelineData.forEach(event => {
    // 确保 parents 数组存在
    if (!event.parents || !Array.isArray(event.parents)) {
      event.parents = [];
    }
    
    // 遍历当前事件的每个 parent
    event.parents.forEach(parentKey => {
      if (parentKey && parentKey.trim() !== "") {
        // 在 timelineData 中查找该 parent 事件
        const parentEvent = timelineData.find(e => e.key === parentKey);
        
        if (parentEvent) {
          // 确保 parent 事件的 kids 数组存在
          if (!parentEvent.kids || !Array.isArray(parentEvent.kids)) {
            parentEvent.kids = [];
          }
          
          // 检查是否已经存在于 parent 的 kids 数组中
          if (!parentEvent.kids.includes(event.key)) {
            parentEvent.kids.push(event.key);
          }
        }
      }
    });
    
    // 同样，遍历当前事件的每个 kid
    if (event.kids && Array.isArray(event.kids)) {
      event.kids.forEach(kidKey => {
        if (kidKey && kidKey.trim() !== "") {
          // 在 timelineData 中查找该 kid 事件
          const kidEvent = timelineData.find(e => e.key === kidKey);
          
          if (kidEvent) {
            // 确保 kid 事件的 parents 数组存在
            if (!kidEvent.parents || !Array.isArray(kidEvent.parents)) {
              kidEvent.parents = [];
            }
            
            // 检查是否已经存在于 kid 的 parents 数组中
            if (!kidEvent.parents.includes(event.key)) {
              kidEvent.parents.push(event.key);
            }
          }
        }
      });
    }
  });
}

// Draw vertical timeline
function drawVerticalTimeline(height, margin) {
  const timelineLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
  timelineLine.setAttribute('x1', margin.left);
  timelineLine.setAttribute('y1', margin.top);
  timelineLine.setAttribute('x2', margin.left);
  timelineLine.setAttribute('y2', height - margin.bottom);
  timelineLine.setAttribute('class', 'timeline-line');
  svgElement.appendChild(timelineLine);
}

// Create year-to-position mapping function
function createYearScale(minYear, maxYear, margin, innerHeight) {
  return (year) => {
    return margin.top + ((year - minYear) / (maxYear - minYear)) * innerHeight;
  };
}


// Add year ticks to timeline
function addYearTicks(minYear, maxYear, yearScale, margin, height) {
  const yearInterval = 10;
  let firstYear = Math.ceil(minYear / 10) * 10;
  if (firstYear > maxYear) {
    firstYear = Math.floor(minYear / 10) * 10;
  }

  for (let year = firstYear; year <= maxYear; year += yearInterval) {
    const y = yearScale(year);

    if (y >= margin.top && y <= height - margin.bottom) {
      // 刻度线
      const tickLine = document.createElementNS('http://www.w3.org/2000/svg', 'line');
      tickLine.setAttribute('x1', margin.left - 5);
      tickLine.setAttribute('y1', y);
      tickLine.setAttribute('x2', margin.left + 5);
      tickLine.setAttribute('y2', y);
      tickLine.setAttribute('stroke', '#7986cb');
      tickLine.setAttribute('stroke-width', 1);
      svgElement.appendChild(tickLine);

      // Year label - use plus/minus signs instead of BC/AD
      const yearLabel = document.createElementNS('http://www.w3.org/2000/svg', 'text');
      yearLabel.setAttribute('x', margin.left - 10);
      yearLabel.setAttribute('y', y + 6);
      yearLabel.setAttribute('text-anchor', 'end');
      yearLabel.setAttribute('font-size', '16');
      yearLabel.setAttribute('fill', '#555');
      yearLabel.setAttribute('font-family', 'Times New Roman');

      let yearDisplay = year < 0 ? `-${Math.abs(year)}` : `${year}`;
      yearLabel.textContent = yearDisplay;
      svgElement.appendChild(yearLabel);
    }
  }
}
