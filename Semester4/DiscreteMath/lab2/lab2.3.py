def select_candidates(vacancy, applicants):
    vacancy_competencies_set = vacancy_competencies[vacancy]
    best_candidates = []
    max_score = 0

    for applicant, competencies in applicants.items():
        score = len(vacancy_competencies_set.intersection(competencies))
        if score > max_score:
            max_score = score
            best_candidates = [applicant]
        elif score == max_score:
            best_candidates.append(applicant)

    return best_candidates


if __name__ == '__main__':    
    vacancy_competencies = {
        'Sales Manager': {'Communication Skills', 'Negotiation Skills', 'Product Knowledge'},
        'Software Developer': {'Programming Skills', 'Analytical Abilities', 'Algorithm Knowledge'},
    }

    applicants = {
        'John': {'Communication Skills', 'Negotiation Skills', 'Product Knowledge'},
        'Alice': {'Analytical Abilities', 'Programming Skills', 'Algorithm Knowledge'},
    }

    vacancy = 'Sales Manager'
    best_candidates = select_candidates(vacancy, applicants)
    print(f"Best candidates for the '{vacancy}' position: {best_candidates}")

    vacancy = 'Software Developer'
    best_candidates = select_candidates(vacancy, applicants)
    print(f"Best candidates for the '{vacancy}' position: {best_candidates}")
