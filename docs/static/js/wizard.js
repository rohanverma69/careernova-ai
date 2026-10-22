/**
 * CareerNova AI - Multi-Step Assessment Wizard Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  const wizardForm = document.getElementById('assessment-wizard-form');
  if (!wizardForm) return;

  let currentStep = 1;
  const totalSteps = 4;

  const btnPrev = document.getElementById('btn-wizard-prev');
  const btnNext = document.getElementById('btn-wizard-next');
  const btnSubmit = document.getElementById('btn-wizard-submit');
  const progressFill = document.getElementById('wizard-progress-fill');

  function updateWizardUI() {
    // Show active pane
    for (let i = 1; i <= totalSteps; i++) {
      const pane = document.getElementById(`step-pane-${i}`);
      const node = document.getElementById(`step-node-${i}`);
      if (pane) {
        pane.classList.toggle('active', i === currentStep);
      }
      if (node) {
        node.classList.toggle('active', i === currentStep);
        node.classList.toggle('completed', i < currentStep);
      }
    }

    // Update progress bar
    if (progressFill) {
      const percentage = ((currentStep - 1) / (totalSteps - 1)) * 100;
      progressFill.style.width = `${percentage}%`;
    }

    // Update button states
    if (btnPrev) {
      btnPrev.style.visibility = currentStep === 1 ? 'hidden' : 'visible';
    }

    if (currentStep === totalSteps) {
      if (btnNext) btnNext.style.display = 'none';
      if (btnSubmit) btnSubmit.style.display = 'inline-flex';
      renderReviewSummary();
    } else {
      if (btnNext) btnNext.style.display = 'inline-flex';
      if (btnSubmit) btnSubmit.style.display = 'none';
    }

    window.scrollTo({ top: wizardForm.offsetTop - 80, behavior: 'smooth' });
  }

  function validateStep(step) {
    if (step === 1) {
      const edu = document.querySelector('[name="education_level"]').value;
      const exp = document.querySelector('[name="experience_years"]').value;
      const style = document.querySelector('[name="work_style"]').value;
      if (!edu || !exp || !style) {
        alert('Please select your education, experience, and work style before proceeding.');
        return false;
      }
    } else if (step === 2) {
      const selectedSkills = document.querySelectorAll('[name="skills"]:checked');
      const customSkills = document.getElementById('custom-skills-input')?.value.trim();
      if (selectedSkills.length === 0 && !customSkills) {
        alert('Please select or add at least 1 technical skill to calibrate recommendations.');
        return false;
      }
    } else if (step === 3) {
      const selectedInterests = document.querySelectorAll('[name="interests"]:checked');
      if (selectedInterests.length === 0) {
        alert('Please select at least 1 domain interest.');
        return false;
      }
    }
    return true;
  }

  if (btnNext) {
    btnNext.addEventListener('click', () => {
      if (validateStep(currentStep)) {
        currentStep = Math.min(totalSteps, currentStep + 1);
        updateWizardUI();
      }
    });
  }

  if (btnPrev) {
    btnPrev.addEventListener('click', () => {
      currentStep = Math.max(1, currentStep - 1);
      updateWizardUI();
    });
  }

  // Clickable step navigation headers (if step previously completed)
  for (let i = 1; i <= totalSteps; i++) {
    const node = document.getElementById(`step-node-${i}`);
    if (node) {
      node.addEventListener('click', () => {
        if (i < currentStep || validateStep(currentStep)) {
          currentStep = i;
          updateWizardUI();
        }
      });
    }
  }

  // Live Skill Search Filter
  const skillSearchInput = document.getElementById('skill-search-input');
  if (skillSearchInput) {
    skillSearchInput.addEventListener('input', (e) => {
      const term = e.target.value.toLowerCase().trim();
      const chips = document.querySelectorAll('#skills-grid .chip-checkbox-label');
      chips.forEach((chip) => {
        const text = chip.textContent.toLowerCase();
        chip.style.display = text.includes(term) ? 'flex' : 'none';
      });
    });
  }

  // Custom Skill Adder
  const btnAddCustom = document.getElementById('btn-add-custom-skill');
  const customInput = document.getElementById('custom-skill-text');
  const customList = document.getElementById('custom-skills-tags');
  const hiddenCustomField = document.getElementById('custom-skills-input');

  const customSkillsArray = [];

  if (btnAddCustom && customInput && customList && hiddenCustomField) {
    function addSkill() {
      const val = customInput.value.trim();
      if (val && !customSkillsArray.includes(val)) {
        customSkillsArray.push(val);
        hiddenCustomField.value = customSkillsArray.join(', ');

        const tag = document.createElement('span');
        tag.className = 'skill-tag skill-tag-gap';
        tag.style.display = 'inline-flex';
        tag.style.alignItems = 'center';
        tag.style.gap = '0.4rem';
        tag.innerHTML = `${val} <span style="cursor:pointer; opacity:0.8;" title="Remove">&times;</span>`;

        tag.querySelector('span').addEventListener('click', () => {
          const idx = customSkillsArray.indexOf(val);
          if (idx > -1) customSkillsArray.splice(idx, 1);
          hiddenCustomField.value = customSkillsArray.join(', ');
          tag.remove();
        });

        customList.appendChild(tag);
        customInput.value = '';
      }
    }

    btnAddCustom.addEventListener('click', addSkill);
    customInput.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        addSkill();
      }
    });
  }

  // Step 4 Review Generator
  function renderReviewSummary() {
    const revEdu = document.getElementById('review-education');
    const revExp = document.getElementById('review-experience');
    const revSkills = document.getElementById('review-skills-count');
    const revInterests = document.getElementById('review-interests-count');

    const eduVal = document.querySelector('[name="education_level"]')?.value || 'Not specified';
    const expVal = document.querySelector('[name="experience_years"]')?.value || 'Not specified';
    const checkedSkills = document.querySelectorAll('[name="skills"]:checked').length + customSkillsArray.length;
    const checkedInterests = document.querySelectorAll('[name="interests"]:checked').length;

    if (revEdu) revEdu.textContent = eduVal;
    if (revExp) revExp.textContent = expVal;
    if (revSkills) revSkills.textContent = `${checkedSkills} skills selected`;
    if (revInterests) revInterests.textContent = `${checkedInterests} interests selected`;
  }

  // Initial UI sync
  updateWizardUI();
});
