/*
 * app.js
 *
 * Talks to the Flask API (/api/airports, /api/flights, /api/milestones)
 * and renders the page: the progress route, the flight-logging form,
 * and the flight history list.
 */

const departureSelect = document.getElementById('departure');
const arrivalSelect = document.getElementById('arrival');
const flightForm = document.getElementById('flightForm');
const formStatus = document.getElementById('formStatus');
const historyList = document.getElementById('historyList');
const totalMilesEl = document.getElementById('totalKm');
const nextLabelEl = document.getElementById('nextLabel');
const routeFillEl = document.getElementById('routeFill');
const routeMarkerEl = document.getElementById('routeMarker');
const waypointsEl = document.getElementById('waypoints');
const factCardEl = document.getElementById('factCard');

// The milestone scale spans 4,000 mi to ~241,850 mi — a log scale keeps
// early progress visible instead of everything bunching up near zero.
function logPosition(mi, minMi, maxMi) {
  if (mi <= 0) return 0;
  const logMin = Math.log(minMi);
  const logMax = Math.log(maxMi);
  const logVal = Math.log(Math.max(mi, minMi));
  return Math.min(100, Math.max(0, ((logVal - logMin) / (logMax - logMin)) * 100));
}

async function loadAirports() {
  const res = await fetch('/api/airports');
  const airports = await res.json();

  for (const select of [departureSelect, arrivalSelect]) {
    for (const a of airports) {
      const opt = document.createElement('option');
      opt.value = a.code;
      opt.textContent = `${a.city} (${a.code}) — ${a.country}`;
      select.appendChild(opt);
    }
  }
}

async function loadMilestones() {
  const res = await fetch('/api/milestones');
  const data = await res.json();

  totalMilesEl.textContent = `${data.total_miles.toLocaleString()} mi`;

  const allMilestones = data.all_milestones;
  const minMi = allMilestones[0].miles;
  const maxMi = allMilestones[allMilestones.length - 1].miles;

  const fillPct = logPosition(data.total_miles, minMi, maxMi);
  routeFillEl.style.width = `${fillPct}%`;
  routeMarkerEl.style.left = `${fillPct}%`;

  waypointsEl.innerHTML = '';
  allMilestones.forEach((m) => {
    const pos = logPosition(m.miles, minMi, maxMi);
    const dot = document.createElement('div');
    dot.className = 'waypoint' + (data.total_miles >= m.miles ? ' reached' : '');
    dot.style.left = `${pos}%`;
    dot.title = `${m.name} — ${m.miles.toLocaleString()} mi`;

    const label = document.createElement('div');
    label.className = 'waypoint-label';
    label.textContent = `L${allMilestones.indexOf(m) + 1}`;
    dot.appendChild(label);

    waypointsEl.appendChild(dot);
  });

  if (data.next_milestone) {
    nextLabelEl.innerHTML = `<strong>${Math.round(data.miles_to_next).toLocaleString()} mi</strong> to go until ${data.next_milestone.name}`;
    factCardEl.innerHTML = `<strong>Next up — ${data.next_milestone.name} (${data.next_milestone.subtitle}):</strong> ${data.next_milestone.fact}`;
  } else if (data.current_milestone) {
    nextLabelEl.innerHTML = `You've hit every milestone — including The Rock Star!`;
    factCardEl.innerHTML = `<strong>${data.current_milestone.name} (${data.current_milestone.subtitle}):</strong> ${data.current_milestone.fact}`;
  } else {
    factCardEl.innerHTML = `Log your first flight to start tracking progress toward The Ocean Cruiser at 4,000 mi.`;
  }
}

async function loadFlights() {
  const res = await fetch('/api/flights');
  const flights = await res.json();

  if (flights.length === 0) {
    historyList.innerHTML = '<div class="empty-state">No flights logged yet — add your first one above.</div>';
    return;
  }

  historyList.innerHTML = '';
  for (const f of flights) {
    const row = document.createElement('div');
    row.className = 'history-row';
    row.innerHTML = `
      <div class="history-route">
        <div class="history-cities">${f.departure_city} (${f.departure_code}) → ${f.arrival_city} (${f.arrival_code})</div>
        <div class="history-meta">${f.flight_date}${f.notes ? ' · ' + escapeHtml(f.notes) : ''}</div>
      </div>
      <div class="history-right">
        <div class="history-distance">${Math.round(f.distance_miles).toLocaleString()} mi</div>
        <button class="delete-btn" data-id="${f.id}" title="Delete flight">×</button>
      </div>
    `;
    historyList.appendChild(row);
  }

  historyList.querySelectorAll('.delete-btn').forEach((btn) => {
    btn.addEventListener('click', () => deleteFlight(btn.dataset.id));
  });
}

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

async function deleteFlight(id) {
  await fetch(`/api/flights/${id}`, { method: 'DELETE' });
  await refreshAll();
}

async function refreshAll() {
  await Promise.all([loadFlights(), loadMilestones()]);
}

flightForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const payload = {
    flight_date: document.getElementById('flightDate').value,
    departure_code: departureSelect.value,
    arrival_code: arrivalSelect.value,
    notes: document.getElementById('notes').value,
  };

  formStatus.textContent = '';
  formStatus.className = 'form-status';

  const res = await fetch('/api/flights', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });

  const result = await res.json();

  if (!res.ok) {
    formStatus.textContent = result.error || 'Something went wrong.';
    formStatus.className = 'form-status error';
    return;
  }

  formStatus.textContent = `Logged: ${payload.departure_code} → ${payload.arrival_code} (${Math.round(result.distance_miles).toLocaleString()} mi)`;
  formStatus.className = 'form-status ok';
  flightForm.reset();

  await refreshAll();
});

(async function init() {
  await loadAirports();
  await refreshAll();
})();
