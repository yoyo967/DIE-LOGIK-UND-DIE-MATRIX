# 3. Android-App: Projektstruktur & Setup

### 3.1 Voraussetzungen

*   Android Studio Ladybug (2024.3+) oder neuer
*   JDK 17
*   Kotlin 2.2.x
*   Android SDK: minSdk 26, targetSdk 35, compileSdk 35
*   Gradle 8.9+ mit Kotlin DSL

---

### 3.2 Projektstruktur (Clean Architecture + Feature Modules)

```
sovereign/
├── app/                              # Application Module
│   ├── src/main/
│   │   ├── java/com/sovereign/app/
│   │   │   ├── SovereignApp.kt       # Application-Klasse (Hilt)
│   │   │   ├── MainActivity.kt       # Single-Activity (Compose)
│   │   │   └── navigation/
│   │   │       ├── SovereignNavGraph.kt
│   │   │       ├── Routes.kt
│   │   │       └── BottomNavBar.kt
│   │   ├── AndroidManifest.xml
│   │   └── res/
│   │       ├── values/
│   │       │   ├── strings.xml
│   │       │   ├── colors.xml        # Sovereign Brand Colors
│   │       │   └── themes.xml
│   │       └── drawable/
│   └── build.gradle.kts
│
├── core/                              # Shared Core Module
│   ├── common/                        # Utility-Klassen, Extensions
│   │   └── src/main/java/com/sovereign/core/common/
│   │       ├── Resource.kt            # Sealed class: Loading/Success/Error
│   │       ├── DateTimeUtils.kt
│   │       ├── CurrencyFormatter.kt
│   │       └── Constants.kt
│   ├── data/                          # Data Layer Abstractions
│   │   └── src/main/java/com/sovereign/core/data/
│   │       ├── remote/
│   │       │   ├── SovereignApi.kt    # Ktor/Retrofit Backend-Interface
│   │       │   ├── dto/               # Data Transfer Objects
│   │       │   │   ├── ContractDto.kt
│   │       │   │   ├── SavingDto.kt
│   │       │   │   ├── ClaimDto.kt
│   │       │   │   └── ApprovalDto.kt
│   │       │   └── interceptors/
│   │       │       └── AuthInterceptor.kt
│   │       ├── local/
│   │       │   ├── SovereignDatabase.kt   # Room DB
│   │       │   ├── dao/
│   │       │   │   ├── ContractDao.kt
│   │       │   │   ├── SavingDao.kt
│   │       │   │   └── ApprovalDao.kt
│   │       │   └── entity/
│   │       │       ├── ContractEntity.kt
│   │       │       ├── SavingEntity.kt
│   │       │       └── ApprovalEntity.kt
│   │       └── repository/
│   │           ├── ContractRepositoryImpl.kt
│   │           ├── SavingRepositoryImpl.kt
│   │           └── ApprovalRepositoryImpl.kt
│   ├── domain/                        # Domain Layer (Use Cases)
│   │   └── src/main/java/com/sovereign/core/domain/
│   │       ├── model/
│   │       │   ├── Contract.kt
│   │       │   ├── Saving.kt
│   │       │   ├── Claim.kt
│   │       │   ├── ApprovalRequest.kt
│   │       │   ├── BoundaryConditions.kt
│   │       │   └── AgentAction.kt
│   │       ├── repository/
│   │       │   ├── ContractRepository.kt      # Interface
│   │       │   ├── SavingRepository.kt
│   │       │   └── ApprovalRepository.kt
│   │       └── usecase/
│   │           ├── GetContractsUseCase.kt
│   │           ├── GetSavingsUseCase.kt
│   │           ├── ApproveActionUseCase.kt
│   │           ├── RejectActionUseCase.kt
│   │           └── SetBoundaryConditionsUseCase.kt
│   └── ui/                            # Shared UI Components
│       └── src/main/java/com/sovereign/core/ui/
│           ├── theme/
│           │   ├── SovereignTheme.kt
│           │   ├── Color.kt
│           │   ├── Typography.kt
│           │   └── Shape.kt
│           ├── components/
│           │   ├── SovereignCard.kt
│           │   ├── SavingsBadge.kt
│           │   ├── ApprovalButton.kt
│           │   ├── StatusIndicator.kt
│           │   ├── MoneyText.kt
│           │   └── LoadingShimmer.kt
│           └── animations/
│               ├── SlideInTransition.kt
│               └── CountUpAnimation.kt
│
├── feature/                           # Feature Modules
│   ├── dashboard/
│   │   └── src/main/java/com/sovereign/feature/dashboard/
│   │       ├── DashboardScreen.kt
│   │       ├── DashboardViewModel.kt
│   │       └── state/
│   │           └── DashboardUiState.kt
│   ├── approvals/
│   │   └── src/main/java/com/sovereign/feature/approvals/
│   │       ├── ApprovalsScreen.kt
│   │       ├── ApprovalsViewModel.kt
│   │       ├── ApprovalDetailScreen.kt
│   │       └── state/
│   │           └── ApprovalsUiState.kt
│   └── onboarding/
│       └── src/main/java/com/sovereign/feature/onboarding/
│           ├── OnboardingScreen.kt
│           └── OnboardingViewModel.kt
│
├── gradle/
│   └── libs.versions.toml             # Version Catalog
├── build.gradle.kts                    # Root Build
└── settings.gradle.kts
```

---

### 3.3 Root `build.gradle.kts`

```kotlin
// Top-level build.gradle.kts
plugins {
    alias(libs.plugins.android.application) apply false
    alias(libs.plugins.android.library) apply false
    alias(libs.plugins.kotlin.android) apply false
    alias(libs.plugins.kotlin.compose) apply false
    alias(libs.plugins.hilt) apply false
    alias(libs.plugins.ksp) apply false
    alias(libs.plugins.google.services) apply false
}
```

---

### 3.4 Version Catalog (`gradle/libs.versions.toml`)

```toml
[versions]
kotlin = "2.2.0"
agp = "8.7.0"
compose-bom = "2025.03.00"
material3 = "1.3.1"
hilt = "2.52"
ksp = "2.2.0-1.0.29"
lifecycle = "2.8.7"
navigation = "2.8.5"
room = "2.7.0"
ktor = "3.0.3"
firebase-bom = "33.7.0"
coroutines = "1.9.0"
coil = "2.7.0"

[libraries]
compose-bom = { group = "androidx.compose", name = "compose-bom", version.ref = "compose-bom" }
compose-ui = { group = "androidx.compose.ui", name = "ui" }
compose-ui-graphics = { group = "androidx.compose.ui", name = "ui-graphics" }
compose-ui-tooling-preview = { group = "androidx.compose.ui", name = "ui-tooling-preview" }
compose-material3 = { group = "androidx.compose.material3", name = "material3" }
compose-material-icons = { group = "androidx.compose.material", name = "material-icons-extended" }

lifecycle-runtime = { group = "androidx.lifecycle", name = "lifecycle-runtime-compose", version.ref = "lifecycle" }
lifecycle-viewmodel = { group = "androidx.lifecycle", name = "lifecycle-viewmodel-compose", version.ref = "lifecycle" }
navigation-compose = { group = "androidx.navigation", name = "navigation-compose", version.ref = "navigation" }

hilt-android = { group = "com.google.dagger", name = "hilt-android", version.ref = "hilt" }
hilt-compiler = { group = "com.google.dagger", name = "hilt-android-compiler", version.ref = "hilt" }
hilt-navigation-compose = { group = "androidx.hilt", name = "hilt-navigation-compose", version = "1.2.0" }

room-runtime = { group = "androidx.room", name = "room-runtime", version.ref = "room" }
room-ktx = { group = "androidx.room", name = "room-ktx", version.ref = "room" }
room-compiler = { group = "androidx.room", name = "room-compiler", version.ref = "room" }

ktor-client-core = { group = "io.ktor", name = "ktor-client-core", version.ref = "ktor" }
ktor-client-okhttp = { group = "io.ktor", name = "ktor-client-okhttp", version.ref = "ktor" }
ktor-client-content-negotiation = { group = "io.ktor", name = "ktor-client-content-negotiation", version.ref = "ktor" }
ktor-serialization-json = { group = "io.ktor", name = "ktor-serialization-kotlinx-json", version.ref = "ktor" }
ktor-client-auth = { group = "io.ktor", name = "ktor-client-auth", version.ref = "ktor" }

firebase-bom = { group = "com.google.firebase", name = "firebase-bom", version.ref = "firebase-bom" }
firebase-auth = { group = "com.google.firebase", name = "firebase-auth-ktx" }
firebase-firestore = { group = "com.google.firebase", name = "firebase-firestore-ktx" }
firebase-messaging = { group = "com.google.firebase", name = "firebase-messaging-ktx" }
firebase-analytics = { group = "com.google.firebase", name = "firebase-analytics-ktx" }

coroutines-core = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-core", version.ref = "coroutines" }
coroutines-android = { group = "org.jetbrains.kotlinx", name = "kotlinx-coroutines-android", version.ref = "coroutines" }
coil-compose = { group = "io.coil-kt", name = "coil-compose", version.ref = "coil" }
kotlinx-serialization-json = { group = "org.jetbrains.kotlinx", name = "kotlinx-serialization-json", version = "1.7.3" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
android-library = { id = "com.android.library", version.ref = "agp" }
kotlin-android = { id = "org.jetbrains.kotlin.android", version.ref = "kotlin" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }
kotlin-serialization = { id = "org.jetbrains.kotlin.plugin.serialization", version.ref = "kotlin" }
hilt = { id = "com.google.dagger.hilt.android", version.ref = "hilt" }
ksp = { id = "com.google.devtools.ksp", version.ref = "ksp" }
google-services = { id = "com.google.gms.google-services", version = "4.4.2" }
```
