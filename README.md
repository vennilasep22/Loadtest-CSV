Performance Testing Guide - 500K Records CSV
📊 Test Data Summary
File: test-data-500k.csv
Records: 500,000
File Size: 30.45 MB
Generation Time: ~8 seconds

Data Distribution
Valid Records: ~450,000 (90%)
Records with Errors: ~50,000 (10%)
Fields: name, email, age, phone, city
Error Types Included
Missing Names (~5,000 records)

Empty name field
Invalid Emails (~15,000 records)

Missing email addresses
Invalid formats: @, test@, test@@example.com
Emails with spaces: test @example.com
Missing domain: test@.example
Invalid Ages (~15,000 records)

Negative ages: -1, -10, -100
Out of range: 200, 250, 999
Empty age field
Invalid Phone Numbers (~15,000 records)

Contains letters: 123-ABC-7890
Invalid text: phone, call-me
Too short: 12-34
Invalid symbols: ###-###-####
🧪 Testing Scenarios
Scenario 1: Basic Load Test
Goal: Test if the application can load and display 500K records

# Upload test-data-500k.csv to the application
# Expected behavior:
# - Page should not crash
# - Loading indicator should appear
# - Data should render in table
# - Validation should run
Expected Performance: - Load Time: 5-15 seconds (depending on browser) - Memory Usage: 200-500 MB - Validation Time: 10-30 seconds

Scenario 2: Validation Performance
Goal: Measure validation speed and accuracy

Metrics to Track: - Time to complete validation - Number of errors detected - CPU usage during validation - Memory consumption

Expected Results: - ~50,000 validation errors detected - Error types correctly identified - No browser freeze or crash

Scenario 3: Editing Performance
Goal: Test inline editing with large dataset

Steps: 1. Load the 500K CSV 2. Edit a cell in first 100 rows 3. Edit a cell in middle rows (around 250K) 4. Edit a cell in last 100 rows 5. Verify real-time validation

Expected Behavior: - Cell editing should be responsive - Validation updates immediately - No lag or performance degradation

Scenario 4: Export Performance
Goal: Test CSV export with large dataset

Steps: 1. Load 500K records 2. Make some edits 3. Click "Export CSV" 4. Measure download time

Expected Performance: - Export preparation: 2-5 seconds - File download starts immediately - Exported file size: ~30 MB

Scenario 5: Browser Compatibility
Test Across Browsers: - Chrome/Edge (Chromium) - Firefox - Safari (if on Mac)

Metrics: - Load time - Memory usage - Responsiveness - Maximum supported records

Scenario 6: Memory Leak Test
Goal: Check for memory leaks over time

Steps: 1. Open browser developer tools 2. Load 500K CSV 3. Monitor memory usage 4. Perform various operations (edit, scroll, validate) 5. Check if memory is released after operations

Expected: - Memory should stabilize after initial load - No continuous memory growth - Garbage collection should free unused memory

🔍 Performance Benchmarks
Expected Performance Metrics
Metric	Expected Value	Notes
Initial Load	5-15 seconds	Depends on browser
Validation	10-30 seconds	All 500K records
Memory Usage	200-500 MB	Peak during validation
Scrolling	Smooth	Virtual scrolling needed
Edit Response	<100ms	Per cell edit
Export Time	2-5 seconds	File preparation
Browser-Specific Performance
Chrome/Edge: - Best performance - Handles large datasets well - ~200-300 MB memory usage

Firefox: - Good performance - Slightly slower than Chrome - ~250-400 MB memory usage

Safari: - Moderate performance - May struggle with 500K records - ~300-500 MB memory usage

⚠️ Known Limitations
Current Component Limitations
The current CSV validator component loads all data into memory at once. With 500,000 records:

Memory Intensive

All 500K rows loaded in React state
All DOM elements rendered
High memory consumption
Slow Rendering

TanStack Table renders all rows
Browser may freeze during initial render
Scrolling might be laggy
No Virtual Scrolling

All rows rendered in DOM
Causes performance issues
Limited by browser capabilities
Recommended Improvements
To handle 500K+ records efficiently:

// 1. Add virtual scrolling
import { useVirtualizer } from '@tanstack/react-virtual'

// 2. Implement pagination
const [page, setPage] = useState(0)
const [pageSize, setPageSize] = useState(100)

// 3. Use worker threads for validation
const worker = new Worker('./validationWorker.js')

// 4. Lazy load data
const [visibleData, setVisibleData] = useState([])
🚀 Performance Optimization Guide
Option 1: Add Virtual Scrolling
npm install @tanstack/react-virtual
Update component to use virtual scrolling:

import { useVirtualizer } from '@tanstack/react-virtual'

// Only render visible rows
const rowVirtualizer = useVirtualizer({
  count: data.length,
  getScrollElement: () => parentRef.current,
  estimateSize: () => 35,
})
Option 2: Implement Pagination
// Show 1000 rows per page
const itemsPerPage = 1000
const totalPages = Math.ceil(data.length / itemsPerPage)
const currentPageData = data.slice(
  currentPage * itemsPerPage,
  (currentPage + 1) * itemsPerPage
)
Option 3: Web Workers for Validation
Create validationWorker.js:

self.onmessage = function(e) {
  const { data } = e.data
  const errors = validateAllData(data)
  self.postMessage({ errors })
}
Option 4: Progressive Loading
// Load and validate in chunks
const chunkSize = 10000
const loadChunk = async (startIndex, endIndex) => {
  const chunk = data.slice(startIndex, endIndex)
  await validateChunk(chunk)
  setProgress((endIndex / data.length) * 100)
}
📈 Performance Testing Tools
Browser DevTools
Chrome DevTools:

1. Open DevTools (F12)
2. Go to Performance tab
3. Click Record
4. Load CSV file
5. Stop recording
6. Analyze timeline
Memory Profiler:

1. DevTools > Memory tab
2. Take heap snapshot before load
3. Load CSV
4. Take another snapshot
5. Compare to find memory leaks
Lighthouse Audit
# Run Lighthouse on the deployed app
npx lighthouse http://your-app-url --view

# Check:
# - Performance score
# - Memory usage
# - Loading time
# - Interactivity metrics
Custom Performance Logging
Add to component:

const measurePerformance = () => {
  const start = performance.now()
  
  // Perform operation
  validateData(data)
  
  const end = performance.now()
  console.log(`Validation took ${end - start}ms`)
}

// Measure memory
console.log('Memory:', performance.memory.usedJSHeapSize / 1048576, 'MB')
🎯 Performance Goals
Target Metrics
✅ Load 100K records: <5 seconds
✅ Load 500K records: <15 seconds
✅ Validation: <30 seconds
✅ Memory: <500 MB
✅ Smooth scrolling: 60 FPS
✅ Edit response: <100ms
✅ Export: <5 seconds
If Performance is Poor
Immediate Actions: 1. Reduce batch size in validation 2. Add loading indicators 3. Implement pagination 4. Use virtual scrolling

Long-term Solutions: 1. Server-side validation API 2. Streaming CSV processing 3. IndexedDB for large datasets 4. Web Workers for background processing

📊 Monitoring Commands
Check File Statistics
# Count total records
wc -l test-data-500k.csv

# Count records with errors
grep -E "^,|,,|-[0-9]+," test-data-500k.csv | wc -l

# Check file size
ls -lh test-data-500k.csv

# View first 10 error records
awk -F',' 'NR>1 && ($1=="" || $2=="" || $3<0 || $3>150)' test-data-500k.csv | head -10
Sample Error Analysis
# Count empty name fields
awk -F',' '$1==""' test-data-500k.csv | wc -l

# Count invalid emails
grep -E "@{2,}|^[^@]+@$|@\." test-data-500k.csv | wc -l

# Count invalid ages
awk -F',' '$3<0 || $3>150' test-data-500k.csv | wc -l

# Count invalid phones
grep -E "ABC|###|call-me|phone" test-data-500k.csv | wc -l
🔧 Troubleshooting Large Files
Issue: Browser Freezes
Solution: 1. Reduce visible rows (implement pagination) 2. Add virtual scrolling 3. Use Web Workers for validation 4. Show loading progress

Issue: Out of Memory
Solution: 1. Close other tabs 2. Increase browser memory limit 3. Process data in chunks 4. Use streaming instead of loading all at once

Issue: Slow Validation
Solution: 1. Optimize validation logic 2. Use memoization 3. Validate only visible rows 4. Move validation to Web Worker

Issue: Export Fails
Solution: 1. Export in chunks 2. Use streaming downloads 3. Compress before download 4. Show progress indicator

📝 Test Report Template
# CSV Validator Performance Test Report

**Date:** [Date]
**Browser:** [Browser Name and Version]
**OS:** [Operating System]
**Hardware:** [CPU, RAM]

## Test Results

### Load Performance
- File size: 30.45 MB
- Load time: [X] seconds
- Records loaded: 500,000
- Memory usage: [X] MB

### Validation Performance
- Validation time: [X] seconds
- Errors detected: [X]
- CPU usage: [X]%
- Memory peak: [X] MB

### Interaction Performance
- Edit response time: [X] ms
- Scroll FPS: [X]
- Export time: [X] seconds

### Issues Encountered
- [List any issues]

### Recommendations
- [List recommendations]
🎓 Learning Outcomes
After testing with 500K records, you'll understand:

Performance Bottlenecks

DOM rendering limits
Memory constraints
Validation performance
Optimization Techniques

Virtual scrolling
Pagination
Web Workers
Lazy loading
Browser Capabilities

Maximum dataset size
Memory management
Rendering performance
Real-world Constraints

User experience trade-offs
Performance vs features
Scalability limits
🚦 Next Steps
Test Basic Functionality

Upload test-data-500k.csv
Verify it loads
Check validation works
Measure Performance

Use browser DevTools
Record metrics
Identify bottlenecks
Optimize If Needed

Implement virtual scrolling
Add pagination
Use Web Workers
Test Again

Verify improvements
Compare metrics
Document results
Remember: The current component is designed for moderate CSV files (<10K rows). For production use with large files (100K+ rows), implement the optimization techniques mentioned above.

Good luck with your performance testing! 🚀


# CSV Processor Vite

This project processes large CSV files with PapaParse and displays them with TanStack Table + virtual scrolling.
Features: multi-file header validation, error summary, row highlighting, export-only-error-rows.

## Quick start

1. Install dependencies:
   ```bash
   npm install
