from django.shortcuts import render, redirect
from .models import CV, PersonalInfo
from .forms import CVForm, PersonalInfoForm, EducationFormSet, ExperienceFormSet, SkillFormSet, CVProjectFormSet

def create_cv(request):
    if request.method == "POST":
        personal_info_form = PersonalInfoForm(request.POST)
        if personal_info_form.is_valid():
            personal_info = personal_info_form.save()
            cv_form = CVForm(request.POST, instance=CV(personal_info=personal_info))
            if cv_form.is_valid():
                cv = cv_form.save()
                education_formset = EducationFormSet(request.POST, instance=cv)
                experience_formset = ExperienceFormSet(request.POST, instance=cv)
                skill_formset = SkillFormSet(request.POST, instance=cv)
                cv_project_formset = CVProjectFormSet(request.POST, request.FILES, instance=cv)
                
                if all([education_formset.is_valid(), experience_formset.is_valid(), skill_formset.is_valid(), cv_project_formset.is_valid()]):
                    education_formset.save()
                    experience_formset.save()
                    skill_formset.save()
                    cv_project_formset.save()
                    return redirect('cv_detail', pk=cv.pk)
    else:
        personal_info_form = PersonalInfoForm()
        cv_form = CVForm()
        education_formset = EducationFormSet()
        experience_formset = ExperienceFormSet()
        skill_formset = SkillFormSet()
        cv_project_formset = CVProjectFormSet()

    return render(request, 'create_cv.html', {
        'personal_info_form': personal_info_form,
        'cv_form': cv_form,
        'education_formset': education_formset,
        'experience_formset': experience_formset,
        'skill_formset': skill_formset,
        'cv_project_formset': cv_project_formset,
    })

def cv_detail(request, pk):
    cv = CV.objects.get(pk=pk)
    return render(request, 'cv_detail.html', {'cv': cv})
