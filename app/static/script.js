/* ── Company card Know More toggle ── */
function toggleDetails(id) {
    const panel = document.getElementById('details-' + id);
    panel.classList.toggle('open');

    // Reset any open aging tables when collapsing the card
    if (!panel.classList.contains('open')) {
        resetAgingPills(id);
    }
}

/* ── Corporate aging panel toggle (called by any KPI strip card click) ── */
function toggleCorporateAging() {
    const panel = document.getElementById('details-corporate');
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
