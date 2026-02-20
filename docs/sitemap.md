# Dinner Planner – Sitemap

## Overview

This document outlines the primary navigation structure for the Dinner Planner application.

The application allows users to:
- Manage dinner recipes
- Plan 2 recipes per week
- Log when recipes were cooked
- View suggestions based on cooking history

---

## Primary Navigation

- Home
- Recipes
- Meal Planner
- Cooking History
- Suggestions

---

## Page Structure

### 1. Home

**Route:** `/`

Purpose:
- Overview of the app
- Quick links to:
  - This Week’s Plan
  - Suggested Recipes
  - Recently Cooked

---

### 2. Recipes

**Route:** `/recipes`

#### 2.1 Recipe List
- Displays all recipes
- Search / filter (future enhancement)
- Link to recipe detail
- Link to add recipe

#### 2.2 Recipe Detail
**Route:** `/recipes/:id`

- Title
- Description
- Ingredients
- Instructions
- “Mark as I've Made This!” button
- Edit recipe

#### 2.3 Add / Edit Recipe
**Route:** `/recipes/new`
**Route:** `/recipes/:id/edit`

- Form to create or update recipe

---

### 3. Meal Planner

**Route:** `/meal-plan`

#### 3.1 Weekly View
- Displays current week
- Shows up to 2 planned recipes
- Option to add recipe

Business Rule:
- Maximum of 2 recipes per week

---

### 4. Cooking History

**Route:** `/history`

- List of all cooking log entries
- Sort by date (newest first)
- Displays:
  - Recipe name
  - Date cooked

---

### 5. Suggestions

**Route:** `/suggestions`

- Displays 5 recipes
- Criteria:
  - Not cooked in the last 60 days
- Randomized results
- Option to add directly to current week

---

## Future Enhancements (Out of Scope for V1)

- User authentication
- Grocery list generation
- Tags / categories
- Dietary filters
- Ratings / notes on cooking log
- Multi-user support