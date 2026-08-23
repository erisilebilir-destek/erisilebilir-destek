// API ve Sunucu Ayarları
const API_BASE_URL = 'http://127.0.0.1:8000';
let AUTH_TOKEN = localStorage.getItem('auth_token') || '';
let CURRENT_USER = 'teknofest';

// Uygulama Durumu (State)
let selectedFile = null;
let currentContentId = null;

// Ekran Okuyucu Durumu
let screenReaderEnabled = false;

// HTML Elementlerini Seçelim
const views = {
    'view-feed': document.getElementById('view-feed'),
    'view-share': document.getElementById('view-share'),
    'view-profile': document.getElementById('view-profile')
};
const navButtons = document.querySelectorAll('.app-nav .nav-item');
const headerTitle = document.getElementById('headerTitle');

// Sayfa Geçiş Yönetimi
function switchView(targetViewId) {
    // Tüm görünümleri gizle, hedefleneni göster
    Object.keys(views).forEach(key => {
        if (views[key]) {
            views[key].classList.remove('active');
        }
    });
    
    if (views[targetViewId]) {
        views[targetViewId].classList.add('active');
    }

    // Aktif navigasyon butonunu işaretle
    navButtons.forEach(btn => {
        btn.classList.remove('active');
        if (btn.dataset.view === targetViewId) {
            btn.classList.add('active');
        }
    });

    // Başlığı güncelle
    if (targetViewId === 'view-feed') {
        headerTitle.textContent = 'Erişilebilir Destek';
        loadFeed();
    } else if (targetViewId === 'view-share') {
        headerTitle.textContent = 'Yeni Gönderi';
    } else if (targetViewId === 'view-profile') {
        headerTitle.textContent = 'Profil';
        loadProfile();
    }
}

// Navigasyon butonlarına tıklama dinleyicileri ekleyelim
navButtons.forEach(button => {
    button.addEventListener('click', () => {
        const targetView = button.dataset.view;
        if (targetView) {
            switchView(targetView);
        } else {
            showToast('Bu özellik yakında aktif olacaktır.');
        }
    });
});

// Toast Mesaj Gösterimi
function showToast(message) {
    const toast = document.getElementById('toast');
    toast.querySelector('.toast-message').textContent = message;
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

// ==========================================
// 1. KULLANICI GİRİŞ/KAYIT SEED İŞLEMLERİ
// ==========================================
async function ensureDemoUserAuthenticated() {
    try {
        // Giriş yapmayı dene
        const loginData = new URLSearchParams();
        loginData.append('username', CURRENT_USER);
        loginData.append('password', 'demo123456');

        let response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            body: loginData,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        });

        if (response.ok) {
            const data = await response.json();
            AUTH_TOKEN = data.access_token;
            localStorage.setItem('auth_token', AUTH_TOKEN);
            return;
        }

        // Giriş başarısızsa kayıt etmeyi dene
        const registerResponse = await fetch(`${API_BASE_URL}/auth/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                kullanici_adi: CURRENT_USER,
                eposta: 'teknofest@nsosyal.com',
                sifre: 'demo123456'
            })
        });

        if (registerResponse.ok) {
            // Tekrar giriş yap
            response = await fetch(`${API_BASE_URL}/auth/login`, {
                method: 'POST',
                body: loginData,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            });
            if (response.ok) {
                const data = await response.json();
                AUTH_TOKEN = data.access_token;
                localStorage.setItem('auth_token', AUTH_TOKEN);
            }
        }
    } catch (error) {
        console.error('Kimlik doğrulama hatası:', error);
    }
}

// ==========================================
// 2. ERİŞİLEBİLİRLİK AYARLARI (ACCESSIBILITY)
// ==========================================
const panelToggle = document.getElementById('panelToggle');
const panelControls = document.getElementById('panelControls');

panelToggle.addEventListener('click', () => {
    const isExpanded = panelToggle.getAttribute('aria-expanded') === 'true';
    panelToggle.setAttribute('aria-expanded', !isExpanded);
    panelControls.hidden = isExpanded;
});

// Yazı Boyutu Ayarları
let fontScale = parseInt(localStorage.getItem('font_scale')) || 100;
document.documentElement.style.setProperty('--font-scale', `${fontScale}%`);

document.getElementById('btnTextInc').addEventListener('click', () => {
    if (fontScale < 150) {
        fontScale += 10;
        updateFontScale();
    }
});

document.getElementById('btnTextDec').addEventListener('click', () => {
    if (fontScale > 80) {
        fontScale -= 10;
        updateFontScale();
    }
});

document.getElementById('btnTextReset').addEventListener('click', () => {
    fontScale = 100;
    updateFontScale();
});

function updateFontScale() {
    document.documentElement.style.setProperty('--font-scale', `${fontScale}%`);
    localStorage.setItem('font_scale', fontScale);
    showToast(`Yazı boyutu: %${fontScale}`);
}

// Yüksek Kontrast Ayarı
const contrastToggle = document.getElementById('contrastToggle');
let isHighContrast = localStorage.getItem('high_contrast') === 'true';

if (isHighContrast) {
    document.body.classList.add('high-contrast');
    contrastToggle.textContent = 'AÇIK';
    contrastToggle.classList.add('active');
}

contrastToggle.addEventListener('click', () => {
    isHighContrast = !isHighContrast;
    if (isHighContrast) {
        document.body.classList.add('high-contrast');
        contrastToggle.textContent = 'AÇIK';
        contrastToggle.classList.add('active');
        contrastToggle.setAttribute('aria-pressed', 'true');
    } else {
        document.body.classList.remove('high-contrast');
        contrastToggle.textContent = 'KAPALI';
        contrastToggle.classList.remove('active');
        contrastToggle.setAttribute('aria-pressed', 'false');
    }
    localStorage.setItem('high_contrast', isHighContrast);
});

// Ekran Okuyucu Simülatörü Ayarı
const screenReaderToggle = document.getElementById('screenReaderToggle');
const voiceControl = document.getElementById('voiceControl');

screenReaderToggle.addEventListener('click', () => {
    screenReaderEnabled = !screenReaderEnabled;
    if (screenReaderEnabled) {
        screenReaderToggle.textContent = 'AÇIK';
        screenReaderToggle.classList.add('active');
        screenReaderToggle.setAttribute('aria-pressed', 'true');
        voiceControl.style.display = 'block';
        speak('Ekran okuyucu simülatörü aktif edildi. Betimlemelerini duymak istediğiniz görsel veya yazılara tıklayabilirsiniz.');
    } else {
        screenReaderToggle.textContent = 'KAPALI';
        screenReaderToggle.classList.remove('active');
        screenReaderToggle.setAttribute('aria-pressed', 'false');
        voiceControl.style.display = 'none';
        if (window.speechSynthesis) {
            window.speechSynthesis.cancel();
        }
    }
});

function speak(text) {
    if (!screenReaderEnabled || !window.speechSynthesis) return;
    window.speechSynthesis.cancel(); // Önceki seslendirmeleri sustur
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'tr-TR';
    window.speechSynthesis.speak(utterance);
}

// Ekran okuyucu tıklandığında seslendirme yapması için sayfa tıklamalarını dinleme
document.addEventListener('click', (e) => {
    if (!screenReaderEnabled) return;
    
    // Erişilebilirlik açıklaması içeren kartlar
    const accBox = e.target.closest('.post-accessibility-info');
    if (accBox) {
        speak(accBox.innerText);
        return;
    }

    const postContent = e.target.closest('.post-content');
    if (postContent) {
        speak(postContent.innerText);
        return;
    }

    const postHeader = e.target.closest('.post-header');
    if (postHeader) {
        speak(postHeader.innerText);
        return;
    }
    
    const badge = e.target.closest('.engelsiz-skor-badge');
    if (badge) {
        speak(badge.innerText);
        return;
    }
});

// ==========================================
// 3. GÖNDERİ PAYLAŞIM VE ANALİZ AKIŞI
// ==========================================
const mediaUploader = document.getElementById('mediaUploader');
const fileInput = document.getElementById('fileInput');
const uploadPlaceholder = document.getElementById('uploadPlaceholder');
const previewContainer = document.getElementById('previewContainer');
const btnCheck = document.getElementById('btnCheck');
const btnShare = document.getElementById('btnShare');
const checkResultPlaceholder = document.getElementById('checkResultPlaceholder');
const checkResults = document.getElementById('checkResults');
const approvedAltText = document.getElementById('approvedAltText');

const resGeneralScore = document.getElementById('resGeneralScore');
const resContrastScore = document.getElementById('resContrastScore');
const resReadabilityScore = document.getElementById('resReadabilityScore');
const accessibilityFeedback = document.getElementById('accessibilityFeedback');
const postDescription = document.getElementById('postDescription');

// Enter & Space ile dosya seçici tetikleme (erişilebilirlik için)
mediaUploader.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        fileInput.click();
    }
});

fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;

    selectedFile = file;
    
    // Önizleme göster
    previewContainer.innerHTML = '';
    const reader = new FileReader();
    
    reader.onload = (event) => {
        if (file.type.startsWith('image/')) {
            const img = document.createElement('img');
            img.src = event.target.result;
            img.alt = 'Yüklenen görsel önizlemesi';
            previewContainer.appendChild(img);
        } else if (file.type.startsWith('video/')) {
            const video = document.createElement('video');
            video.src = event.target.result;
            video.controls = true;
            previewContainer.appendChild(video);
        }
        uploadPlaceholder.style.display = 'none';
        previewContainer.style.display = 'flex';
        btnCheck.disabled = false;
        
        // Önceki sonuçları sıfırla
        checkResultPlaceholder.style.display = 'block';
        checkResults.style.display = 'none';
        btnShare.disabled = true;
        currentContentId = null;
    };
    
    reader.readAsDataURL(file);
});

// "Kontrol Et" Butonu Tıklaması (API'ye gönderme)
btnCheck.addEventListener('click', async () => {
    if (!selectedFile) return;

    btnCheck.disabled = true;
    btnCheck.textContent = 'Analiz ediliyor...';
    checkResultPlaceholder.textContent = 'Yapay zeka erişilebilirlik analizi yapıyor, lütfen bekleyin...';

    const formData = new FormData();
    formData.append('dosya', selectedFile);

    const headers = {};
    if (AUTH_TOKEN) {
        headers['Authorization'] = `Bearer ${AUTH_TOKEN}`;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/api/v1/analyze`, {
            method: 'POST',
            headers: headers,
            body: formData
        });

        if (!response.ok) {
            throw new Error('Analiz isteği başarısız oldu.');
        }

        const data = await response.json();
        currentContentId = data.content_id;

        // Skorları doldur
        const res = data.sonuc;
        resGeneralScore.textContent = res.genel_erisilebilirlik_puani || 100;
        resContrastScore.textContent = res.renk_kontrast_skoru ? res.renk_kontrast_skoru.toFixed(1) : '4.5';
        resReadabilityScore.textContent = res.okunabilirlik_skoru ? res.okunabilirlik_skoru.toFixed(0) : '85';

        // Geri bildirim metnini ayarla
        let feedback = '';
        if (res.genel_erisilebilirlik_puani >= 90) {
            feedback = '🌟 Harika! İçeriğiniz yüksek erişilebilirlik standartlarına sahip. Alternatif metin ve altyazı alanları başarıyla hazırlandı.';
        } else if (res.genel_erisilebilirlik_puani >= 70) {
            feedback = '⚠️ İçeriğiniz genel olarak iyi durumda. Renk kontrastını iyileştirerek veya metni daha sade hale getirerek erişilebilirliği artırabilirsiniz.';
        } else {
            feedback = '🛑 Düşük erişilebilirlik puanı! Görme ve işitme engelli kullanıcıların içeriğinizi anlaması zor olabilir. Alternatif metinleri gözden geçirin.';
        }
        accessibilityFeedback.textContent = feedback;

        // Önerilen alternatif metni doldur
        approvedAltText.value = res.otomatik_alt_text || '';

        // UI Güncelle
        checkResultPlaceholder.style.display = 'none';
        checkResults.style.display = 'block';
        btnShare.disabled = false;
        showToast('Erişilebilirlik analizi tamamlandı!');
        
        if (screenReaderEnabled) {
            speak(`Analiz tamamlandı. İçeriğinizin erişilebilirlik puanı yüz üzerinden ${res.genel_erisilebilirlik_puani}. Alternatif metin önerisi: ${res.otomatik_alt_text}`);
        }

    } catch (error) {
        console.error('Analiz hatası:', error);
        checkResultPlaceholder.textContent = 'Hata oluştu: Sunucuya bağlanılamadı ya da desteklenmeyen bir dosya türü yüklediniz.';
        showToast('Analiz sırasında bir hata oluştu.');
    } finally {
        btnCheck.disabled = false;
        btnCheck.textContent = 'Kontrol Et';
    }
});

// "Paylaş" Butonu Tıklaması (Gönderiyi Yayınlama)
btnShare.addEventListener('click', async () => {
    if (!currentContentId) return;

    btnShare.disabled = true;
    btnShare.textContent = 'Paylaşılıyor...';

    const payload = {
        orijinal_metin: postDescription.value,
        otomatik_alt_text: approvedAltText.value,
        onaylandi_mi: true
    };

    const headers = {
        'Content-Type': 'application/json'
    };
    if (AUTH_TOKEN) {
        headers['Authorization'] = `Bearer ${AUTH_TOKEN}`;
    }

    try {
        const response = await fetch(`${API_BASE_URL}/api/v1/posts/${currentContentId}/publish`, {
            method: 'POST',
            headers: headers,
            body: JSON.stringify(payload)
        });

        if (!response.ok) {
            throw new Error('Gönderi paylaşılamadı.');
        }

        showToast('Gönderiniz başarıyla paylaşıldı!');
        
        // Alanları temizle
        postDescription.value = '';
        approvedAltText.value = '';
        fileInput.value = '';
        selectedFile = null;
        currentContentId = null;
        
        uploadPlaceholder.style.display = 'block';
        previewContainer.style.display = 'none';
        checkResultPlaceholder.style.display = 'block';
        checkResults.style.display = 'none';
        btnCheck.disabled = true;

        // Akış sekmesine yönlendir
        switchView('view-feed');

    } catch (error) {
        console.error('Yayınlama hatası:', error);
        showToast('Gönderi paylaşılırken hata oluştu.');
    } finally {
        btnShare.disabled = false;
        btnShare.textContent = 'Paylaş';
    }
});

// ==========================================
// 4. VERİ YÜKLEME: AKIŞ VE PROFİL
// ==========================================

// Gönderi Akışını Yükle
async function loadFeed() {
    const feedContainer = document.getElementById('feedContainer');
    
    try {
        const response = await fetch(`${API_BASE_URL}/api/v1/posts`);
        if (!response.ok) {
            throw new Error('Akış verileri alınamadı.');
        }

        const posts = await response.json();
        feedContainer.innerHTML = '';

        if (posts.length === 0) {
            feedContainer.innerHTML = `
                <div class="feed-placeholder">
                    <i class="fa-solid fa-folder-open"></i>
                    <p>Henüz paylaşılmış bir gönderi bulunmuyor.</p>
                </div>
            `;
            return;
        }

        posts.forEach(post => {
            const card = document.createElement('div');
            card.className = 'post-card';
            
            // Medya yolu dönüşümü (Windows ters eğik çizgilerini düzelt)
            const cleanMediaPath = post.dosya_yolu ? post.dosya_yolu.replace(/\\/g, '/') : '';
            const mediaUrl = `${API_BASE_URL}/${cleanMediaPath}`;
            
            const isVideo = cleanMediaPath.endsWith('.mp4') || cleanMediaPath.endsWith('.webm') || cleanMediaPath.endsWith('.mov');
            
            let mediaHtml = '';
            if (post.dosya_yolu) {
                if (isVideo) {
                    mediaHtml = `<video src="${mediaUrl}" controls aria-label="Gönderi videosu"></video>`;
                } else {
                    mediaHtml = `<img src="${mediaUrl}" alt="${post.analiz?.otomatik_alt_text || 'Erişilebilir görsel'}">`;
                }
            }

            // Alternatif metin bilgisi kutusu
            let accessibilityInfoHtml = '';
            if (post.analiz?.otomatik_alt_text) {
                accessibilityInfoHtml = `
                    <div class="post-accessibility-info" tabindex="0">
                        <div class="info-title">
                            <i class="fa-solid fa-universal-access"></i>
                            <span>Erişilebilirlik Bilgisi</span>
                        </div>
                        <div class="info-body">
                            ${post.analiz.otomatik_alt_text}
                        </div>
                    </div>
                `;
            }

            const username = post.user?.kullanici_adi || 'teknofest';
            const displayName = username.charAt(0).toUpperCase() + username.slice(1);

            card.innerHTML = `
                <div class="post-header">
                    <img src="https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=100&auto=format&fit=crop&q=80" alt="${displayName} Avatar" class="user-avatar-small">
                    <div class="post-user-info">
                        <span class="post-username">${displayName}</span>
                        <span class="post-handle">@${username}</span>
                    </div>
                </div>
                <div class="post-media-container">
                    ${mediaHtml}
                </div>
                ${accessibilityInfoHtml}
                <div class="post-actions">
                    <i class="fa-regular fa-heart" aria-label="Beğen"></i>
                    <i class="fa-regular fa-comment" aria-label="Yorum Yap"></i>
                    <i class="fa-regular fa-paper-plane" aria-label="Paylaş"></i>
                </div>
                <div class="post-content">
                    <div class="post-text">
                        <strong>@${username}</strong> ${post.orijinal_metin || ''}
                    </div>
                </div>
            `;
            feedContainer.appendChild(card);
        });

    } catch (error) {
        console.error('Akış yükleme hatası:', error);
        feedContainer.innerHTML = `
            <div class="feed-placeholder">
                <i class="fa-solid fa-triangle-exclamation"></i>
                <p>Uzak sunucu bağlantı hatası.</p>
                <span>Lütfen backend uygulamasını çalıştırın.</span>
            </div>
        `;
    }
}

// Profil Verilerini Yükle
async function loadProfile() {
    const profileScore = document.getElementById('profileScore');
    const profilePostCount = document.getElementById('profilePostCount');
    const profileMediaGrid = document.getElementById('profileMediaGrid');

    try {
        // 1. Profil Puanı ve Gönderi Sayısı Al
        const scoreRes = await fetch(`${API_BASE_URL}/api/v1/users/${CURRENT_USER}/score`);
        if (scoreRes.ok) {
            const scoreData = await scoreRes.json();
            profileScore.textContent = scoreData.score;
        }

        // 2. Profil Gönderilerini Al
        const postsRes = await fetch(`${API_BASE_URL}/api/v1/users/${CURRENT_USER}/posts`);
        if (!postsRes.ok) throw new Error('Profil gönderileri alınamadı.');

        const posts = await postsRes.json();
        profilePostCount.textContent = posts.length;
        profileMediaGrid.innerHTML = '';

        if (posts.length === 0) {
            profileMediaGrid.innerHTML = `
                <div style="grid-column: span 3; text-align: center; padding: 40px; color: var(--text-secondary);">
                    <i class="fa-solid fa-images" style="font-size: 24px; margin-bottom: 8px;"></i>
                    <p>Henüz yüklenmiş medya yok.</p>
                </div>
            `;
            return;
        }

        posts.forEach(post => {
            if (!post.dosya_yolu) return;

            const gridItem = document.createElement('div');
            gridItem.className = 'grid-item';
            
            const cleanMediaPath = post.dosya_yolu.replace(/\\/g, '/');
            const mediaUrl = `${API_BASE_URL}/${cleanMediaPath}`;
            const isVideo = cleanMediaPath.endsWith('.mp4') || cleanMediaPath.endsWith('.webm') || cleanMediaPath.endsWith('.mov');

            const score = post.analiz?.genel_erisilebilirlik_puani || 100;
            const scoreClass = score < 70 ? 'low-score' : '';
            
            let itemHtml = '';
            if (isVideo) {
                itemHtml = `<video src="${mediaUrl}#t=0.5" preload="metadata"></video>`;
            } else {
                itemHtml = `<img src="${mediaUrl}" alt="${post.analiz?.otomatik_alt_text || 'Medya'}">`;
            }

            gridItem.innerHTML = `
                ${itemHtml}
                <div class="grid-accessibility-badge ${scoreClass}" aria-label="Erişilebilirlik Puanı: ${score}">
                    <i class="fa-solid fa-universal-access"></i> ${score}
                </div>
            `;

            // Profildeki görsele tıklandığında ekran okuyucu seslendirsin
            gridItem.addEventListener('click', () => {
                if (post.analiz?.otomatik_alt_text) {
                    speak(`Seçili profil gönderisi açıklaması: ${post.analiz.otomatik_alt_text}. Erişilebilirlik puanı ${score}.`);
                }
            });

            profileMediaGrid.appendChild(gridItem);
        });

    } catch (error) {
        console.error('Profil yükleme hatası:', error);
        profileMediaGrid.innerHTML = `
            <div style="grid-column: span 3; text-align: center; padding: 20px; color: var(--text-secondary);">
                <i class="fa-solid fa-exclamation-triangle"></i>
                <p>Profil yüklenemedi.</p>
            </div>
        `;
    }
}

// ==========================================
// BAŞLANGIÇ ÇALIŞTIRICISI (INIT)
// ==========================================
window.addEventListener('DOMContentLoaded', async () => {
    // Demo kullanıcıyı doğrula veya kaydet
    await ensureDemoUserAuthenticated();
    
    // Varsayılan görünümü aç (Gönderi Akışı)
    switchView('view-feed');
});
