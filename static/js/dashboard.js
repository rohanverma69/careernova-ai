/**
 * CareerNova AI - Dashboard & Bookmark Controller
 */

// Show interactive toast alert
function showToast(message, type = 'info') {
  const container = document.querySelector('.alert-container') || (() => {
    const c = document.createElement('div');
    c.className = 'alert-container';
    document.body.appendChild(c);
    return c;
  })();

  const alert = document.createElement('div');
  alert.className = `alert alert-${type}`;
  alert.innerHTML = `
    <span>${message}</span>
    <button class="alert-close" aria-label="Close">&times;</button>
  `;

  alert.querySelector('.alert-close').addEventListener('click', () => alert.remove());
  container.appendChild(alert);

  setTimeout(() => {
    alert.style.opacity = '0';
    setTimeout(() => alert.remove(), 400);
  }, 4500);
}

// Bookmark / Unbookmark Career
async function toggleSaveCareer(careerKey, buttonElement) {
  const csrfToken = window.getCSRFToken ? window.getCSRFToken() : '';

  try {
    const resp = await fetch('/api/careers/toggle-save', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({ career_key: careerKey })
    });

    if (resp.status === 401) {
      window.location.href = '/login?next=' + encodeURIComponent(window.location.pathname);
      return;
    }

    const data = await resp.json();
    if (data.success) {
      showToast(data.message, 'success');
      if (buttonElement) {
        if (data.saved) {
          buttonElement.classList.add('btn-primary');
          buttonElement.classList.remove('btn-secondary');
          buttonElement.innerHTML = '★ Saved to Dashboard';
        } else {
          buttonElement.classList.remove('btn-primary');
          buttonElement.classList.add('btn-secondary');
          buttonElement.innerHTML = '☆ Save Career Path';
        }
      }
    } else {
      showToast(data.error || 'Could not update saved career.', 'danger');
    }
  } catch (err) {
    showToast('Network error while saving career.', 'danger');
  }
}

// Update Skill Progress Status (To Learn -> In Progress -> Completed)
async function updateSkillStatus(skillName, newStatus, selectElement) {
  const csrfToken = window.getCSRFToken ? window.getCSRFToken() : '';

  try {
    const resp = await fetch('/api/skills/update-status', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({ skill_name: skillName, status: newStatus })
    });

    const data = await resp.json();
    if (data.success) {
      showToast(data.message, 'success');
      // If we are on the kanban board, refresh after a short delay
      if (document.querySelector('.kanban-board')) {
        setTimeout(() => window.location.reload(), 450);
      }
    } else {
      showToast(data.error || 'Failed to update skill.', 'danger');
    }
  } catch (err) {
    showToast('Network error updating skill.', 'danger');
  }
}

// Remove tracked skill
async function deleteSkill(skillName, buttonElement) {
  if (!confirm(`Are you sure you want to remove "${skillName}" from your tracked skills?`)) return;

  const csrfToken = window.getCSRFToken ? window.getCSRFToken() : '';

  try {
    const resp = await fetch('/api/skills/delete', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken
      },
      body: JSON.stringify({ skill_name: skillName })
    });

    const data = await resp.json();
    if (data.success) {
      showToast(data.message, 'info');
      const itemRow = buttonElement.closest('.kanban-item') || buttonElement.closest('tr');
      if (itemRow) itemRow.remove();
    }
  } catch (err) {
    showToast('Failed to delete skill.', 'danger');
  }
}
