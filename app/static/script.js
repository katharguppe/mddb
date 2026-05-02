/* ── Company card Know More toggle ── */
function toggleDetails(id) {
    const panel = document.getElementById('details-' + id);
    if (!panel) return;
    const isOpen = panel.classList.contains('open');
    panel.classList.toggle('open');

    // Update button text
    const btn = document.querySelector('.company-card .btn-know-more[onclick="toggleDetails(\'' + id + '\')"]');
    if (btn) btn.textContent = isOpen ? 'Know More \u2192' : 'Close \u2191';

    if (!isOpen) {
        // Opening: default to Revenue tab
        switchKpiTab(id, 'revenue');
    } else {
        // Closing: reset aging pills in case Payments tab was active
        resetAgingPills(id);
    }
}

/* ── KPI tab switching ── */
function switchKpiTab(companyId, tabKey) {
    const container = document.getElementById('kpi-tabs-' + companyId);
    if (!container) return;

    // Deactivate all tabs and hide all panels
    container.querySelectorAll('.kpi-tab').forEach(function(tab) {
        tab.classList.remove('active');
    });
    container.querySelectorAll('.kpi-tab-panel').forEach(function(p) {
        p.classList.remove('active');
    });

    // Activate the selected tab and panel
    const activeTab = container.querySelector('[data-tab="' + tabKey + '"]');
    if (activeTab) activeTab.classList.add('active');

    const activePanel = document.getElementById('kpi-panel-' + companyId + '-' + tabKey);
    if (activePanel) activePanel.classList.add('active');
}

/* ── Corporate aging panel toggle (called by any KPI strip card click) ── */
function toggleCorporateAging() {
    const panel = document.getElementById('details-corporate');
    if (!panel) return;
    panel.classList.toggle('open');

    if (!panel.classList.contains('open')) {
        resetAgingPills('corporate');
    }
}

/* ── Aging bucket pill toggle ── */
function toggleAgingBucket(companyId, bucket) {
    const pillsContainer = document.getElementById('aging-pills-' + companyId);
    if (!pillsContainer) return;

    const clickedPill = pillsContainer.querySelector(
        '[data-company="' + companyId + '"][data-bucket="' + bucket + '"]'
    );
    const targetTable = document.getElementById(
        'aging-table-' + companyId + '-' + bucket
    );
    if (!clickedPill || !targetTable) return;

    const isAlreadyOpen = clickedPill.classList.contains('active');

    // Close all pills + tables for this company
    resetAgingPills(companyId);

    if (!isAlreadyOpen) {
        // Open the clicked one
        clickedPill.classList.add('active');
        targetTable.classList.add('open');
    }
}

/* ── Helper: close all pills + tables for a given company ── */
function resetAgingPills(companyId) {
    const pillsContainer = document.getElementById('aging-pills-' + companyId);
    if (!pillsContainer) return;

    pillsContainer.querySelectorAll('.aging-pill').forEach(function(pill) {
        pill.classList.remove('active');
    });

    // Close all table wrappers for this company
    document.querySelectorAll('[id^="aging-table-' + companyId + '-"]').forEach(function(table) {
        table.classList.remove('open');
    });
}

/* ── Time-period filter ── */
function setTimePeriod(period) {
    // Update active pill
    document.querySelectorAll('.tf-pill').forEach(function(pill) {
        pill.classList.toggle('active', pill.textContent.trim() === period);
    });

    // Show Weekly Pulse only on WTD
    var pulse = document.getElementById('weekly-pulse-section');
    if (pulse) {
        pulse.classList.toggle('hidden', period !== 'WTD');
    }
}

/* ── Weekly Pulse KPI selector ── */
function switchPulseKpi(kpi) {
    // Update active pill
    document.querySelectorAll('.pulse-kpi-pill').forEach(function(pill) {
        pill.classList.toggle('active', pill.textContent.trim().toLowerCase() === kpi);
    });
    // Show spans for selected KPI, hide others
    document.querySelectorAll('.pulse-kpi-val').forEach(function(span) {
        span.style.display = span.dataset.kpi === kpi ? '' : 'none';
    });
}

/* ── Sticky Notes widget ── */
(function initStickyNotes() {
    var saved = localStorage.getItem('md_notes');
    if (saved) {
        var ta = document.getElementById('sticky-notes-ta');
        if (ta) {
            ta.value = saved;
            updateStickyCharCount();
        }
    }
})();

function toggleStickyNotes() {
    var widget = document.getElementById('sticky-notes');
    if (widget) widget.classList.toggle('sticky-notes--collapsed');
}

function saveStickyNotes() {
    var ta = document.getElementById('sticky-notes-ta');
    if (ta) localStorage.setItem('md_notes', ta.value);
}

function updateStickyCharCount() {
    var ta = document.getElementById('sticky-notes-ta');
    var counter = document.getElementById('sticky-notes-charcount');
    if (ta && counter) counter.textContent = ta.value.length + ' chars';
}

/* ── Print / Export ── */
function printDashboard() {
    // Expand all detail panels
    document.querySelectorAll('.company-details').forEach(function(p) {
        p.classList.add('open');
    });
    // Switch all company KPI tabs to Revenue (no hardcoded slugs)
    document.querySelectorAll('.kpi-tabs-container').forEach(function(container) {
        var id = container.id.replace('kpi-tabs-', '');
        switchKpiTab(id, 'revenue');
    });
    window.print();
}

window.onafterprint = function() {
    document.querySelectorAll('.company-details').forEach(function(p) {
        p.classList.remove('open');
    });
};
