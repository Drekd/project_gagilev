let allCars = []; 
let filteredCars = [];


async function loadAllCars() {
    const container = document.getElementById('carsContainer');
    if (!container) return;
    
    try {
        const response = await fetch('/api/cars/');
        const data = await response.json();
        allCars = data.cars;
        filteredCars = [...allCars];
        displayCars(filteredCars);
        updateResultsCount();
    } catch (error) {
        console.error('Ошибка загрузки:', error);
        if (container) {
            container.innerHTML = '<div style="text-align: center; padding: 40px; color: red;">❌ Ошибка загрузки данных. Проверьте соединение.</div>';
        }
    }
}

function displayCars(cars) {
    const container = document.getElementById('carsContainer');
    if (!container) return;
    
    if (cars.length === 0) {
        container.innerHTML = `
            <div style="grid-column: 1 / -1; text-align: center; padding: 60px;">
                <p style="font-size: 18px; color: var(--text-secondary, #666);">🚗 Автомобили не найдены</p>
                <p style="color: var(--text-secondary, #666); margin-top: 10px;">Попробуйте изменить параметры поиска</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = cars.map(car => `
        <div class="car-card detailed" data-car-id="${car.id}">
            <div class="car-badge ${car.year > 2023 ? 'new' : 'used'}">
                ${car.year > 2023 ? 'Новый' : 'С пробегом'}
            </div>
            <img src="${car.image_url}" alt="${escapeHtml(car.name)}" class="car-image" 
                 onerror="this.src='/static/image/584x438.webp'">
            <div class="car-info">
                <h3 class="car-name">${escapeHtml(car.name)}</h3>
                <div class="car-price">${Number(car.price).toLocaleString('ru-RU')} ₽</div>
                <div class="car-specs">
                    <div class="spec-item">
                        <span class="spec-label">Год:</span>
                        <span class="spec-value">${car.year}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Комплектация:</span>
                        <span class="spec-value">${escapeHtml(car.equipment)}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Цвет:</span>
                        <span class="spec-value">${escapeHtml(car.colour)}</span>
                    </div>
                    <div class="spec-item">
                        <span class="spec-label">Категория:</span>
                        <span class="spec-value">${escapeHtml(car.category)}</span>
                    </div>
                </div>
                <div class="car-actions">
                    <a href="/cars/${car.id}/" class="btn primary">Подробнее</a>
                </div>
            </div>
        </div>
    `).join('');
}

function escapeHtml(str) {
    if (!str) return '';
    return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
}

function applyFilters() {
    const brand = document.getElementById('car-brand')?.value || '';
    const minPrice = document.getElementById('min-price')?.value || '';
    const maxPrice = document.getElementById('max-price')?.value || '';
    const year = document.getElementById('car-year')?.value || '';
    const category = document.getElementById('car-category')?.value || '';
    
    filteredCars = allCars.filter(car => {
        if (brand && !car.name.startsWith(brand)) return false;
        
        const price = Number(car.price);
        if (minPrice && price < Number(minPrice)) return false;
        if (maxPrice && price > Number(maxPrice)) return false;
        if (year && car.year !== Number(year)) return false;
        if (category && car.category !== category) return false;
        
        return true;
    });
    
    displayCars(filteredCars);
    updateResultsCount();
    updatePageTitle(brand);
}

function resetAllFilters() {
    const brandSelect = document.getElementById('car-brand');
    const minPriceInput = document.getElementById('min-price');
    const maxPriceInput = document.getElementById('max-price');
    const yearSelect = document.getElementById('car-year');
    const categorySelect = document.getElementById('car-category');
    
    if (brandSelect) brandSelect.value = '';
    if (minPriceInput) minPriceInput.value = '';
    if (maxPriceInput) maxPriceInput.value = '';
    if (yearSelect) yearSelect.value = '';
    if (categorySelect) categorySelect.value = '';
    
    filteredCars = [...allCars];
    displayCars(filteredCars);
    updateResultsCount();
    updatePageTitle('');
}

function updateResultsCount() {
    const countSpan = document.querySelector('#resultsCount span');
    if (countSpan) {
        countSpan.textContent = filteredCars.length;
    }
}

function updatePageTitle(brand) {
    const titleEl = document.getElementById('pageTitle');
    if (titleEl) {
        if (brand) {
            titleEl.textContent = `Каталог автомобилей ${brand}`;
        } else {
            titleEl.textContent = 'Каталог автомобилей';
        }
    }
}
function validatePriceRange() {
    const minInput = document.getElementById('min-price');
    const maxInput = document.getElementById('max-price');
    
    if (minInput && maxInput && minInput.value && maxInput.value) {
        const min = parseInt(minInput.value);
        const max = parseInt(maxInput.value);
        
        if (min > max) {
            alert('⚠️ Минимальная цена не может быть больше максимальной');
            minInput.value = '';
            return false;
        }
    }
    return true;
}
function initFilters() {
    // Загружаем автомобили
    loadAllCars();
    const selects = ['car-brand', 'car-year', 'car-category'];
    selects.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.addEventListener('change', applyFilters);
        }
    });
    const minPrice = document.getElementById('min-price');
    const maxPrice = document.getElementById('max-price');
    
    if (minPrice) {
        minPrice.addEventListener('input', function() {
            validatePriceRange();
            applyFilters();
        });
    }
    
    if (maxPrice) {
        maxPrice.addEventListener('input', function() {
            validatePriceRange();
            applyFilters();
        });
    }
}

function initTheme() {
    const savedTheme = localStorage.getItem('theme');
    const toggleBtn = document.getElementById('themeToggle');
    
    if (savedTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        if (toggleBtn) toggleBtn.textContent = '☀️';
    }
    
    if (toggleBtn) {
        toggleBtn.addEventListener('click', function() {
            const currentTheme = document.documentElement.getAttribute('data-theme');
            if (currentTheme === 'dark') {
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem('theme', 'light');
                this.textContent = '🌙';
            } else {
                document.documentElement.setAttribute('data-theme', 'dark');
                localStorage.setItem('theme', 'dark');
                this.textContent = '☀️';
            }
        });
    }
}

function showContactForm() {
    const modal = document.getElementById('contactModal');
    if (modal) modal.style.display = 'block';
}

function closeModal() {
    const modal = document.getElementById('contactModal');
    if (modal) modal.style.display = 'none';
}

function initModal() {
    const modal = document.getElementById('contactModal');
    const form = document.getElementById('contactForm');
    
    if (!modal || !form) return;
    
    window.onclick = function(event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    };
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        alert('✅ Ваш запрос отправлен! С вами свяжутся в ближайшее время.');
        closeModal();
        form.reset();
    });
}

function scheduleTestDrive() {
    const sellerPhone = document.querySelector('.seller-phone')?.textContent || '+78001234567';
    window.location.href = `tel:${sellerPhone.replace(/[^0-9+]/g, '')}`;
}

function changeMainImage(imageUrl) {
    const mainImage = document.getElementById('mainCarImage');
    if (mainImage) {
        mainImage.src = imageUrl;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const isCatalogPage = document.getElementById('carsContainer') !== null;
    const isDetailPage = document.getElementById('mainCarImage') !== null;
    
    if (isCatalogPage) {
        initFilters();
    }
    
    if (isDetailPage) {
        initModal();
    }
    
    initTheme();
});