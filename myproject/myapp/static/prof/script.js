document.addEventListener('DOMContentLoaded', function() {
    const profileImage = document.getElementById('profileImage');
    const profileImageInput = document.getElementById('profileImageInput');
    const changePictureBtn = document.getElementById('changePictureBtn');

    const editButtons = document.querySelectorAll('.edit-btn');
    const editSection = document.querySelector('.edit-section');
    const profileSection = document.querySelector('.profile-section');
    const cancelEditBtn = document.getElementById('cancelEditBtn');
    const editForm = document.getElementById('editForm');

    const usernameDisplay = document.getElementById('usernameDisplay');
    const emailDisplay = document.getElementById('emailDisplay');
    const passwordDisplay = document.getElementById('passwordDisplay');

    const usernameInput = document.getElementById('usernameInput');
    const emailInput = document.getElementById('emailInput');
    const passwordInput = document.getElementById('passwordInput');

    // تغییر عکس پروفایل
    changePictureBtn.addEventListener('click', function() {
        profileImageInput.click();
    });

    profileImageInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                profileImage.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });

    // ویرایش اطلاعات
    editButtons.forEach(function(btn) {
        btn.addEventListener('click', function() {
            const field = btn.getAttribute('data-field');
            openEditSection(field);
        });
    });

    function openEditSection(field) {
        profileSection.style.display = 'none';
        editSection.style.display = 'block';

        // پر کردن فرم با مقادیر فعلی
        usernameInput.value = usernameDisplay.textContent;
        emailInput.value = emailDisplay.textContent;
        passwordInput.value = ''; // رمز عبور را خالی می‌گذاریم
    }

    // لغو ویرایش
    cancelEditBtn.addEventListener('click', function() {
        editSection.style.display = 'none';
        profileSection.style.display = 'flex';
    });

    // ذخیره تغییرات
    editForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // اینجا می‌توانید کد ارسال اطلاعات به سرور را اضافه کنید

        // به‌روزرسانی نمایش اطلاعات
        usernameDisplay.textContent = usernameInput.value;
        emailDisplay.textContent = emailInput.value;
        if (passwordInput.value) {
            passwordDisplay.textContent = '********';
        }

        // بازگشت به بخش پروفایل
        editSection.style.display = 'none';
        profileSection.style.display = 'flex';

        alert('تغییرات با موفقیت ذخیره شد!');
    });
});
document.addEventListener('DOMContentLoaded', function() {
    const completeProfileBtn = document.getElementById('completeProfileBtn');
    const completeProfileSection = document.getElementById('completeProfileSection');
    const progressCircle = document.getElementById('progressCircle');
    const progressPercentage = document.getElementById('progressPercentage');

    // فرض کنید درصد تکمیل پروفایل فعلی 50% است.
    let profileCompletion = 50;

    // به‌روزرسانی درصد و دایره پیشرفت
    function updateProgressCircle(percentage) {
        progressCircle.style.background = `conic-gradient(#4CAF50 ${percentage}%, #ccc ${percentage}%)`;
        progressPercentage.textContent = `${percentage}%`;
    }

    updateProgressCircle(profileCompletion);

    // باز کردن فرم تکمیل پروفایل
    completeProfileBtn.addEventListener('click', function() {
        completeProfileSection.style.display = 'block';
        // اینجا می‌توانید هر نوع انتقال اسکرول به بخش فرم را هم اضافه کنید.
    });

    // فرض کنید پس از تکمیل فرم درصد پیشرفت به‌روزرسانی می‌شود.
    document.getElementById('completeProfileForm').addEventListener('submit', function(event) {
        event.preventDefault();

        // به‌روزرسانی درصد تکمیل پروفایل (برای مثال به 100%)
        profileCompletion = 100;
        updateProgressCircle(profileCompletion);

        completeProfileSection.style.display = 'none';
        alert('پروفایل شما با موفقیت تکمیل شد!');
    });
});
