# 4. UI/UX-Architektur (Jetpack Compose)

### 4.1 Design-System: Sovereign Brand Identity

```kotlin
// core/ui/theme/Color.kt
package com.sovereign.core.ui.theme

import androidx.compose.ui.graphics.Color

// Primary Palette
val SovereignNavy = Color(0xFF0A1628)       // Tiefes Navy — Trust & Authority
val SovereignTeal = Color(0xFF00D4AA)       // Teal — Savings & Success
val SovereignGold = Color(0xFFFFB800)       // Gold — Money & Premium
val SovereignWhite = Color(0xFFF8FAFE)      // Off-White — Clean Background

// Status Colors
val SovereignSuccess = Color(0xFF00C853)    // Grün — Aktion erfolgreich
val SovereignWarning = Color(0xFFFF9100)    // Orange — Approval benötigt
val SovereignError = Color(0xFFFF1744)      // Rot — Fehler / Rejected
val SovereignPending = Color(0xFF448AFF)    // Blau — In Bearbeitung

// Surface Colors
val SovereignSurfaceLight = Color(0xFFFFFFFF)
val SovereignSurfaceDark = Color(0xFF0D1B2A)
val SovereignCardLight = Color(0xFFF0F4FA)
val SovereignCardDark = Color(0xFF1B2838)

// Agent Colors (für Dashboard-Unterscheidung)
val AgentNegotiation = Color(0xFF7C4DFF)    // Violett
val AgentSwitching = Color(0xFF00B0FF)      // Cyan
val AgentClaim = Color(0xFFFF6D00)          // Orange
```

```kotlin
// core/ui/theme/Typography.kt
package com.sovereign.core.ui.theme

import androidx.compose.material3.Typography
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.sp
import com.sovereign.core.ui.R

val InterFontFamily = FontFamily(
    Font(R.font.inter_regular, FontWeight.Normal),
    Font(R.font.inter_medium, FontWeight.Medium),
    Font(R.font.inter_semibold, FontWeight.SemiBold),
    Font(R.font.inter_bold, FontWeight.Bold),
)

val SpaceGroteskFamily = FontFamily(
    Font(R.font.space_grotesk_bold, FontWeight.Bold),
)

val SovereignTypography = Typography(
    displayLarge = TextStyle(
        fontFamily = SpaceGroteskFamily,
        fontWeight = FontWeight.Bold,
        fontSize = 57.sp,
        lineHeight = 64.sp,
        letterSpacing = (-0.25).sp
    ),
    headlineLarge = TextStyle(
        fontFamily = SpaceGroteskFamily,
        fontWeight = FontWeight.Bold,
        fontSize = 32.sp,
        lineHeight = 40.sp
    ),
    headlineMedium = TextStyle(
        fontFamily = InterFontFamily,
        fontWeight = FontWeight.SemiBold,
        fontSize = 28.sp,
        lineHeight = 36.sp
    ),
    titleLarge = TextStyle(
        fontFamily = InterFontFamily,
        fontWeight = FontWeight.SemiBold,
        fontSize = 22.sp,
        lineHeight = 28.sp
    ),
    titleMedium = TextStyle(
        fontFamily = InterFontFamily,
        fontWeight = FontWeight.Medium,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.15.sp
    ),
    bodyLarge = TextStyle(
        fontFamily = InterFontFamily,
        fontWeight = FontWeight.Normal,
        fontSize = 16.sp,
        lineHeight = 24.sp,
        letterSpacing = 0.5.sp
    ),
    bodyMedium = TextStyle(
        fontFamily = InterFontFamily,
        fontWeight = FontWeight.Normal,
        fontSize = 14.sp,
        lineHeight = 20.sp,
        letterSpacing = 0.25.sp
    ),
    labelLarge = TextStyle(
        fontFamily = InterFontFamily,
        fontWeight = FontWeight.Medium,
        fontSize = 14.sp,
        lineHeight = 20.sp,
        letterSpacing = 0.1.sp
    ),
    labelSmall = TextStyle(
        fontFamily = InterFontFamily,
        fontWeight = FontWeight.Medium,
        fontSize = 11.sp,
        lineHeight = 16.sp,
        letterSpacing = 0.5.sp
    )
)
```

---

### 4.2 Navigation-Graph

```kotlin
// app/navigation/Routes.kt
package com.sovereign.app.navigation

sealed class Routes(val route: String) {
    data object Dashboard : Routes("dashboard")
    data object Approvals : Routes("approvals")
    data object Contracts : Routes("contracts")
    data object Claims : Routes("claims")
    data object Settings : Routes("settings")

    data object ApprovalDetail : Routes("approvals/{approvalId}") {
        fun createRoute(approvalId: String) = "approvals/$approvalId"
    }
    data object ContractDetail : Routes("contracts/{contractId}") {
        fun createRoute(contractId: String) = "contracts/$contractId"
    }
    data object ClaimDetail : Routes("claims/{claimId}") {
        fun createRoute(claimId: String) = "claims/$claimId"
    }

    data object Onboarding : Routes("onboarding")
    data object BoundaryConditions : Routes("settings/boundaries")
    data object ConnectedAccounts : Routes("settings/accounts")
    data object PaymentSettings : Routes("settings/payment")
}
```

```kotlin
// app/navigation/SovereignNavGraph.kt
package com.sovereign.app.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.navArgument
import androidx.navigation.NavType
import com.sovereign.feature.dashboard.DashboardScreen
import com.sovereign.feature.approvals.ApprovalsScreen
import com.sovereign.feature.approvals.ApprovalDetailScreen
import com.sovereign.feature.contracts.ContractsScreen
import com.sovereign.feature.claims.ClaimsScreen
import com.sovereign.feature.settings.SettingsScreen
import com.sovereign.feature.onboarding.OnboardingScreen

@Composable
fun SovereignNavGraph(
    navController: NavHostController,
    startDestination: String = Routes.Dashboard.route
) {
    NavHost(
        navController = navController,
        startDestination = startDestination
    ) {
        composable(Routes.Dashboard.route) {
            DashboardScreen(
                onApprovalClick = { id ->
                    navController.navigate(Routes.ApprovalDetail.createRoute(id))
                }
            )
        }

        composable(Routes.Approvals.route) {
            ApprovalsScreen(
                onApprovalClick = { id ->
                    navController.navigate(Routes.ApprovalDetail.createRoute(id))
                }
            )
        }

        composable(
            route = Routes.ApprovalDetail.route,
            arguments = listOf(navArgument("approvalId") { type = NavType.StringType })
        ) { backStackEntry ->
            val approvalId = backStackEntry.arguments?.getString("approvalId") ?: return@composable
            ApprovalDetailScreen(
                approvalId = approvalId,
                onBack = { navController.popBackStack() }
            )
        }

        composable(Routes.Contracts.route) {
            ContractsScreen(
                onContractClick = { id ->
                    navController.navigate(Routes.ContractDetail.createRoute(id))
                }
            )
        }

        composable(Routes.Claims.route) {
            ClaimsScreen(
                onClaimClick = { id ->
                    navController.navigate(Routes.ClaimDetail.createRoute(id))
                }
            )
        }

        composable(Routes.Settings.route) {
            SettingsScreen(navController = navController)
        }

        composable(Routes.Onboarding.route) {
            OnboardingScreen(
                onComplete = {
                    navController.navigate(Routes.Dashboard.route) {
                        popUpTo(Routes.Onboarding.route) { inclusive = true }
                    }
                }
            )
        }
    }
}
```

---

### 4.3 Dashboard-Screen (Kernstück der App)

```kotlin
// feature/dashboard/DashboardScreen.kt
package com.sovereign.feature.dashboard

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import com.sovereign.core.ui.theme.*
import com.sovereign.feature.dashboard.components.*
import com.sovereign.feature.dashboard.state.DashboardUiState

@Composable
fun DashboardScreen(
    onApprovalClick: (String) -> Unit,
    viewModel: DashboardViewModel = hiltViewModel()
) {
    val uiState by viewModel.uiState.collectAsState()

    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 16.dp),
        verticalArrangement = Arrangement.spacedBy(16.dp),
        contentPadding = PaddingValues(vertical = 24.dp)
    ) {
        item {
            SavingsSummaryCard(
                totalSaved = uiState.totalSavedEuro,
                monthSaved = uiState.monthSavedEuro,
                savingsGrowthPercent = uiState.savingsGrowthPercent
            )
        }

        if (uiState.pendingApprovals.isNotEmpty()) {
            item {
                Text(
                    text = "Wartet auf deine Freigabe",
                    style = MaterialTheme.typography.titleMedium,
                    modifier = Modifier.padding(top = 8.dp)
                )
            }
            items(uiState.pendingApprovals.size) { index ->
                val approval = uiState.pendingApprovals[index]
                ApprovalCard(
                    approval = approval,
                    onClick = { onApprovalClick(approval.id) },
                    onQuickApprove = { viewModel.quickApprove(approval.id) },
                    onQuickReject = { viewModel.quickReject(approval.id) }
                )
            }
        }

        item {
            ActiveAgentsCard(
                agents = uiState.agentStatuses
            )
        }

        item {
            Text(
                text = "Letzte Aktivitäten",
                style = MaterialTheme.typography.titleMedium,
                modifier = Modifier.padding(top = 8.dp)
            )
        }
        items(uiState.recentActions.size) { index ->
            RecentActionItem(action = uiState.recentActions[index])
        }
    }
}
```

---

### 4.4 Swipe-to-Approve Komponente

```kotlin
// feature/approvals/components/SwipeToApprove.kt
package com.sovereign.feature.approvals.components

import androidx.compose.animation.animateColorAsState
import androidx.compose.foundation.background
import androidx.compose.foundation.gestures.detectHorizontalDragGestures
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Check
import androidx.compose.material.icons.filled.Close
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.input.pointer.pointerInput
import androidx.compose.ui.unit.IntOffset
import androidx.compose.ui.unit.dp
import com.sovereign.core.ui.theme.*
import kotlin.math.roundToInt

@Composable
fun SwipeToApprove(
    onApprove: () -> Unit,
    onReject: () -> Unit,
    modifier: Modifier = Modifier
) {
    var offsetX by remember { mutableFloatStateOf(0f) }
    val threshold = 200f

    val backgroundColor by animateColorAsState(
        when {
            offsetX > threshold * 0.5f -> SovereignSuccess.copy(alpha = 0.2f)
            offsetX < -threshold * 0.5f -> SovereignError.copy(alpha = 0.2f)
            else -> MaterialTheme.colorScheme.surfaceVariant
        },
        label = "swipe_bg"
    )

    Box(
        modifier = modifier
            .fillMaxWidth()
            .height(64.dp)
            .clip(RoundedCornerShape(32.dp))
            .background(backgroundColor)
    ) {
        Icon(
            imageVector = Icons.Default.Close,
            contentDescription = "Ablehnen",
            tint = SovereignError,
            modifier = Modifier
                .align(Alignment.CenterStart)
                .padding(start = 20.dp)
        )

        Icon(
            imageVector = Icons.Default.Check,
            contentDescription = "Freigeben",
            tint = SovereignSuccess,
            modifier = Modifier
                .align(Alignment.CenterEnd)
                .padding(end = 20.dp)
        )

        Surface(
            modifier = Modifier
                .offset { IntOffset(offsetX.roundToInt(), 0) }
                .align(Alignment.Center)
                .size(56.dp)
                .pointerInput(Unit) {
                    detectHorizontalDragGestures(
                        onDragEnd = {
                            when {
                                offsetX > threshold -> onApprove()
                                offsetX < -threshold -> onReject()
                            }
                            offsetX = 0f
                        }
                    ) { _, dragAmount ->
                        offsetX += dragAmount
                    }
                },
            shape = RoundedCornerShape(28.dp),
            color = SovereignTeal,
            shadowElevation = 4.dp
        ) {
            Box(contentAlignment = Alignment.Center) {
                Text(
                    text = "⟷",
                    style = MaterialTheme.typography.titleLarge,
                    color = SovereignNavy
                )
            }
        }
    }
}
```
