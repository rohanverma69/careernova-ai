/**
 * CareerNova AI - Radar Chart & Score Visualizer
 * Pure vanilla HTML5 Canvas implementation (Zero external bloat).
 */

class SkillRadarChart {
  constructor(canvasId, dimensionsData) {
    this.canvas = document.getElementById(canvasId);
    if (!this.canvas) return;

    this.ctx = this.canvas.getContext('2d');
    this.dimensions = dimensionsData || {
      "Software Engineering": 60,
      "AI & Data Science": 75,
      "Cloud & DevOps": 50,
      "Security & Systems": 40,
      "Product & Strategy": 65,
      "UI/UX Design": 45
    };

    this.keys = Object.keys(this.dimensions);
    this.numAxes = this.keys.length;
    this.angleStep = (Math.PI * 2) / this.numAxes;
    this.animationProgress = 0;

    this.init();
  }

  init() {
    this.resize();
    window.addEventListener('resize', () => {
      this.resize();
      this.draw(1);
    });
    this.animate();
  }

  resize() {
    const rect = this.canvas.parentElement.getBoundingClientRect();
    const size = Math.min(rect.width, 360);
    this.canvas.width = size * window.devicePixelRatio;
    this.canvas.height = size * window.devicePixelRatio;
    this.canvas.style.width = `${size}px`;
    this.canvas.style.height = `${size}px`;
    this.ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    this.width = size;
    this.height = size;
    this.centerX = size / 2;
    this.centerY = size / 2;
    this.radius = size * 0.36;
  }

  animate() {
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (prefersReduced) {
      this.draw(1);
      return;
    }

    const startTime = performance.now();
    const duration = 900;

    const step = (time) => {
      const elapsed = time - startTime;
      this.animationProgress = Math.min(1, elapsed / duration);
      // Ease out cubic
      const eased = 1 - Math.pow(1 - this.animationProgress, 3);
      this.draw(eased);

      if (this.animationProgress < 1) {
        requestAnimationFrame(step);
      }
    };

    requestAnimationFrame(step);
  }

  draw(progress) {
    this.ctx.clearRect(0, 0, this.width, this.height);

    // 1. Draw concentric background polygon webs
    const levels = 4;
    for (let l = 1; l <= levels; l++) {
      const levelRadius = (this.radius / levels) * l;
      this.ctx.beginPath();
      for (let i = 0; i < this.numAxes; i++) {
        const angle = i * this.angleStep - Math.PI / 2;
        const x = this.centerX + Math.cos(angle) * levelRadius;
        const y = this.centerY + Math.sin(angle) * levelRadius;
        if (i === 0) this.ctx.moveTo(x, y);
        else this.ctx.lineTo(x, y);
      }
      this.ctx.closePath();
      this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
      this.ctx.lineWidth = 1;
      this.ctx.stroke();
    }

    // 2. Draw radial axis spokes and labels
    for (let i = 0; i < this.numAxes; i++) {
      const angle = i * this.angleStep - Math.PI / 2;
      const x = this.centerX + Math.cos(angle) * this.radius;
      const y = this.centerY + Math.sin(angle) * this.radius;

      this.ctx.beginPath();
      this.ctx.moveTo(this.centerX, this.centerY);
      this.ctx.lineTo(x, y);
      this.ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
      this.ctx.stroke();

      // Axis labels
      const labelX = this.centerX + Math.cos(angle) * (this.radius + 24);
      const labelY = this.centerY + Math.sin(angle) * (this.radius + 20);

      this.ctx.fillStyle = '#94a3b8';
      this.ctx.font = '600 10.5px Inter, sans-serif';
      this.ctx.textAlign = 'center';
      this.ctx.textBaseline = 'middle';

      const keyText = this.keys[i];
      // Simple split for long label formatting
      const parts = keyText.split(' ');
      if (parts.length > 1) {
        this.ctx.fillText(parts[0], labelX, labelY - 5);
        this.ctx.fillText(parts.slice(1).join(' '), labelX, labelY + 7);
      } else {
        this.ctx.fillText(keyText, labelX, labelY);
      }
    }

    // 3. Draw user data polygon
    this.ctx.beginPath();
    const points = [];
    for (let i = 0; i < this.numAxes; i++) {
      const val = this.dimensions[this.keys[i]] || 20;
      const r = (this.radius * (val / 100)) * progress;
      const angle = i * this.angleStep - Math.PI / 2;
      const x = this.centerX + Math.cos(angle) * r;
      const y = this.centerY + Math.sin(angle) * r;
      points.push({ x, y, val });
      if (i === 0) this.ctx.moveTo(x, y);
      else this.ctx.lineTo(x, y);
    }
    this.ctx.closePath();

    // Fill with glowing purple/cyan gradient
    const grad = this.ctx.createRadialGradient(
      this.centerX, this.centerY, 10,
      this.centerX, this.centerY, this.radius
    );
    grad.addColorStop(0, 'rgba(139, 92, 246, 0.45)');
    grad.addColorStop(1, 'rgba(6, 182, 212, 0.25)');

    this.ctx.fillStyle = grad;
    this.ctx.fill();

    this.ctx.strokeStyle = '#06b6d4';
    this.ctx.lineWidth = 2.5;
    this.ctx.shadowBlur = 12;
    this.ctx.shadowColor = '#06b6d4';
    this.ctx.stroke();
    this.ctx.shadowBlur = 0;

    // 4. Draw node dots on vertices
    points.forEach((p) => {
      this.ctx.beginPath();
      this.ctx.arc(p.x, p.y, 4.5, 0, Math.PI * 2);
      this.ctx.fillStyle = '#ffffff';
      this.ctx.fill();
      this.ctx.strokeStyle = '#8b5cf6';
      this.ctx.lineWidth = 2;
      this.ctx.stroke();
    });
  }
}

// Circular Score Counter Animator
function animateScoreNumbers() {
  const counters = document.querySelectorAll('[data-target-score]');
  counters.forEach((counter) => {
    const target = parseInt(counter.getAttribute('data-target-score'), 10) || 0;
    const duration = 1200;
    const startTime = performance.now();

    function updateCount(time) {
      const elapsed = time - startTime;
      const progress = Math.min(1, elapsed / duration);
      const current = Math.floor(progress * target);
      counter.textContent = `${current}%`;

      if (progress < 1) {
        requestAnimationFrame(updateCount);
      } else {
        counter.textContent = `${target}%`;
      }
    }

    requestAnimationFrame(updateCount);
  });
}

document.addEventListener('DOMContentLoaded', () => {
  animateScoreNumbers();
});
