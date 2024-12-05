const content = {
    about: {
        title: "درباره ما",
        text: "معرفی شورای نگهبان و وظایف آن در تدوین و بررسی لوایح."
    },
    services: {
        title: "خدمات ما",
        text: "بررسی لوایح، مطالعات حقوقی و آموزش قوانین توسط کارشناسان مجرب."
    },
    news: {
        title: "اخبار و مقالات",
        text: "جدیدترین اخبار و مقالات حوزه قوانین و لوایح را دنبال کنید."
    },
    membership: {
        title: "عضویت",
        text: "برای عضویت در تیم لایحه نویسی شورای نگهبان درخواست دهید."
    },
    contact: {
        title: "تماس با ما",
        text: "آدرس: تهران، میدان انقلاب | تلفن: ۰۲۱-۱۲۳۴۵۶۷۸"
    }
};

function showMore(section) {
    document.getElementById("modalTitle").innerText = content[section].title;
    document.getElementById("modalText").innerText = content[section].text;
    document.getElementById("moreModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("moreModal").style.display = "none";
}
// باز و بسته شدن سوالات متداول
document.querySelectorAll(".faq-item h3").forEach(question => {
    question.addEventListener("click", () => {
        const faqItem = question.parentElement;
        faqItem.classList.toggle("active");
    });
});

