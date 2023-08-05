// faithful$eruptions
// results compared to R density function
// to view violin plot in R
// p <- ggplot(mtcars, aes(factor(cyl), mpg))
// p + geom_violin(scale = "width") + geom_boxplot(width=0.1)
// p

import {boxplotStats, density, nrd0} from './kde';

const eruptions = [3.600, 1.800, 3.333, 2.283, 4.533, 2.883, 4.700, 3.600, 1.950, 4.350, 1.833, 3.917, 4.200, 1.750, 4.700, 2.167, 1.750, 4.800, 1.600, 4.250, 1.800
    , 1.750, 3.450, 3.067, 4.533, 3.600, 1.967, 4.083, 3.850, 4.433, 4.300, 4.467, 3.367, 4.033, 3.833, 2.017, 1.867, 4.833, 1.833, 4.783, 4.350, 1.883
    , 4.567, 1.750, 4.533, 3.317, 3.833, 2.100, 4.633, 2.000, 4.800, 4.716, 1.833, 4.833, 1.733, 4.883, 3.717, 1.667, 4.567, 4.317, 2.233, 4.500, 1.750
    , 4.800, 1.817, 4.400, 4.167, 4.700, 2.067, 4.700, 4.033, 1.967, 4.500, 4.000, 1.983, 5.067, 2.017, 4.567, 3.883, 3.600, 4.133, 4.333, 4.100, 2.633
    , 4.067, 4.933, 3.950, 4.517, 2.167, 4.000, 2.200, 4.333, 1.867, 4.817, 1.833, 4.300, 4.667, 3.750, 1.867, 4.900, 2.483, 4.367, 2.100, 4.500, 4.050
    , 1.867, 4.700, 1.783, 4.850, 3.683, 4.733, 2.300, 4.900, 4.417, 1.700, 4.633, 2.317, 4.600, 1.817, 4.417, 2.617, 4.067, 4.250, 1.967, 4.600, 3.767
    , 1.917, 4.500, 2.267, 4.650, 1.867, 4.167, 2.800, 4.333, 1.833, 4.383, 1.883, 4.933, 2.033, 3.733, 4.233, 2.233, 4.533, 4.817, 4.333, 1.983, 4.633
    , 2.017, 5.100, 1.800, 5.033, 4.000, 2.400, 4.600, 3.567, 4.000, 4.500, 4.083, 1.800, 3.967, 2.200, 4.150, 2.000, 3.833, 3.500, 4.583, 2.367, 5.000
    , 1.933, 4.617, 1.917, 2.083, 4.583, 3.333, 4.167, 4.333, 4.500, 2.417, 4.000, 4.167, 1.883, 4.583, 4.250, 3.767, 2.033, 4.433, 4.083, 1.833, 4.417
    , 2.183, 4.800, 1.833, 4.800, 4.100, 3.966, 4.233, 3.500, 4.366, 2.250, 4.667, 2.100, 4.350, 4.133, 1.867, 4.600, 1.783, 4.367, 3.850, 1.933, 4.500
    , 2.383, 4.700, 1.867, 3.833, 3.417, 4.233, 2.400, 4.800, 2.000, 4.150, 1.867, 4.267, 1.750, 4.483, 4.000, 4.117, 4.083, 4.267, 3.917, 4.550, 4.083
    , 2.417, 4.183, 2.217, 4.450, 1.883, 1.850, 4.283, 3.950, 2.333, 4.150, 2.350, 4.933, 2.900, 4.583, 3.833, 2.083, 4.367, 2.133, 4.350, 2.200, 4.450
    , 3.567, 4.500, 4.150, 3.817, 3.917, 4.450, 2.000, 4.283, 4.767, 4.533, 1.850, 4.250, 1.983, 2.250, 4.750, 4.117, 2.150, 4.417, 1.817, 4.467];


it('nrd0', () => {
    // bw.nrd0(faithful$eruptions)
    expect(nrd0(boxplotStats(eruptions))).toBeCloseTo(0.334777);
    eruptions.push(NaN);
    expect(nrd0(boxplotStats(eruptions))).toBeCloseTo(0.334777);
});
it('nrd0-zeros', () => {
    // bw.nrd0(c(0,0,0))
    expect(nrd0(boxplotStats([0, 0, 0]))).toBeCloseTo(0.7224674);
});
it('nrd0-zeros-nans', () => {
    expect(nrd0(boxplotStats([0, 0, NaN, 0, NaN]))).toBeCloseTo(0.7224674);
});
// it('nrd', () => {
//     // bw.nrd(faithful$eruptions)
//     expect(nrd(eruptions)).toBeCloseTo(0.394293);
// });
// it('nrd-zeros', () => {
//     // bw.nrd(c(0,0,0))
//     expect(nrd([0, 0, 0])).toBeCloseTo(0);
// });

it('density', () => {
    // density(faithful$eruptions, n=200, cut=0)
    const x = [1.6, 1.61758793969849, 1.63517587939699, 1.65276381909548, 1.67035175879397, 1.68793969849246, 1.70552763819095, 1.72311557788945, 1.74070351758794, 1.75829145728643, 1.77587939698492, 1.79346733668342, 1.81105527638191, 1.8286432160804, 1.84623115577889, 1.86381909547739, 1.88140703517588, 1.89899497487437, 1.91658291457286, 1.93417085427136, 1.95175879396985, 1.96934673366834, 1.98693467336683, 2.00452261306533, 2.02211055276382, 2.03969849246231, 2.0572864321608, 2.0748743718593, 2.09246231155779, 2.11005025125628, 2.12763819095477, 2.14522613065327, 2.16281407035176, 2.18040201005025, 2.19798994974874, 2.21557788944724, 2.23316582914573, 2.25075376884422, 2.26834170854271, 2.28592964824121, 2.3035175879397, 2.32110552763819, 2.33869346733668, 2.35628140703518, 2.37386934673367, 2.39145728643216, 2.40904522613065, 2.42663316582915, 2.44422110552764, 2.46180904522613, 2.47939698492462, 2.49698492462312, 2.51457286432161, 2.5321608040201, 2.54974874371859, 2.56733668341709, 2.58492462311558, 2.60251256281407, 2.62010050251256, 2.63768844221106, 2.65527638190955, 2.67286432160804, 2.69045226130653, 2.70804020100503, 2.72562814070352, 2.74321608040201, 2.7608040201005, 2.778391959799, 2.79597989949749, 2.81356783919598, 2.83115577889447, 2.84874371859296, 2.86633165829146, 2.88391959798995, 2.90150753768844, 2.91909547738693, 2.93668341708543, 2.95427135678392, 2.97185929648241, 2.9894472361809, 3.0070351758794, 3.02462311557789, 3.04221105527638, 3.05979899497487, 3.07738693467337, 3.09497487437186, 3.11256281407035, 3.13015075376884, 3.14773869346734, 3.16532663316583, 3.18291457286432, 3.20050251256281, 3.21809045226131, 3.2356783919598, 3.25326633165829, 3.27085427135678, 3.28844221105528, 3.30603015075377, 3.32361809045226, 3.34120603015075, 3.35879396984925, 3.37638190954774, 3.39396984924623, 3.41155778894472, 3.42914572864322, 3.44673366834171, 3.4643216080402, 3.48190954773869, 3.49949748743719, 3.51708542713568, 3.53467336683417, 3.55226130653266, 3.56984924623116, 3.58743718592965, 3.60502512562814, 3.62261306532663, 3.64020100502513, 3.65778894472362, 3.67537688442211, 3.6929648241206, 3.71055276381909, 3.72814070351759, 3.74572864321608, 3.76331658291457, 3.78090452261306, 3.79849246231156, 3.81608040201005, 3.83366834170854, 3.85125628140703, 3.86884422110553, 3.88643216080402, 3.90402010050251, 3.921608040201, 3.9391959798995, 3.95678391959799, 3.97437185929648, 3.99195979899497, 4.00954773869347, 4.02713567839196, 4.04472361809045, 4.06231155778894, 4.07989949748744, 4.09748743718593, 4.11507537688442, 4.13266331658291, 4.15025125628141, 4.1678391959799, 4.18542713567839, 4.20301507537688, 4.22060301507538, 4.23819095477387, 4.25577889447236, 4.27336683417085, 4.29095477386935, 4.30854271356784, 4.32613065326633, 4.34371859296482, 4.36130653266332, 4.37889447236181, 4.3964824120603, 4.41407035175879, 4.43165829145729, 4.44924623115578, 4.46683417085427, 4.48442211055276, 4.50201005025126, 4.51959798994975, 4.53718592964824, 4.55477386934673, 4.57236180904523, 4.58994974874372, 4.60753768844221, 4.6251256281407, 4.64271356783919, 4.66030150753769, 4.67788944723618, 4.69547738693467, 4.71306532663317, 4.73065326633166, 4.74824120603015, 4.76582914572864, 4.78341708542714, 4.80100502512563, 4.81859296482412, 4.83618090452261, 4.85376884422111, 4.8713567839196, 4.88894472361809, 4.90653266331658, 4.92412060301507, 4.94170854271357, 4.95929648241206, 4.97688442211055, 4.99447236180904, 5.01206030150754, 5.02964824120603, 5.04723618090452, 5.06482412060301, 5.08241206030151, 5.1];
    const y = [0.213478578608861, 0.223018824044235, 0.232466580991117, 0.241784600972171, 0.250913309124478, 0.259837795238423, 0.268468317412609, 0.276819207323014, 0.284787145364743, 0.292390504608097, 0.299543688282911, 0.306243572500786, 0.312442061134668, 0.318102413238931, 0.323227304088532, 0.327736901376939, 0.33169435163241, 0.334970634076671, 0.337677285674051, 0.339686396785247, 0.341095852516339, 0.341829022790568, 0.3419367969595, 0.341405596960868, 0.340238647921777, 0.338483120958335, 0.336097701381124, 0.33318390539777, 0.329662357322423, 0.325665859650331, 0.321125809912578, 0.31615052968827, 0.31071758129624, 0.30489175951099, 0.298694406805154, 0.292156749542548, 0.285330959497092, 0.278225865486313, 0.270910851327782, 0.263383940425202, 0.255715143878892, 0.247912378841307, 0.240026906429416, 0.232082293165237, 0.224112972118739, 0.21614881618199, 0.208218402030495, 0.200346652988886, 0.192565994339995, 0.184886868628464, 0.177353707030034, 0.169959182910237, 0.162753210939254, 0.155723415972902, 0.148909461108963, 0.142308462622891, 0.135941154322499, 0.129819862930597, 0.123941929815001, 0.118338974657826, 0.112982165929037, 0.107925026072107, 0.103118011388865, 0.0986175405885534, 0.0943790585894366, 0.09043899404576, 0.0867749331622153, 0.0833975739306874, 0.0803075020502305, 0.0774899213885538, 0.0749684794467482, 0.0727037516422235, 0.0707419462114788, 0.0690265810112251, 0.0676066236796921, 0.0664337254419164, 0.0655378490075724, 0.0648940595069019, 0.0645092226315097, 0.0643808160215046, 0.0644939213404546, 0.0648673628560272, 0.065465690947445, 0.0663280371111002, 0.0674048527934992, 0.068738710096057, 0.0702872328589571, 0.0720771266256605, 0.0740867473937719, 0.0763230623318329, 0.0787842355346883, 0.0814583367001842, 0.084362539265835, 0.0874667087257143, 0.0908063430650981, 0.0943382793752182, 0.0981019106133754, 0.102059587960305, 0.10623671092626, 0.110614030954778, 0.115198916502523, 0.119989902831086, 0.124976751559869, 0.130175141904552, 0.135557670243638, 0.141156412749194, 0.146931408384521, 0.152918006045914, 0.15908048342126, 0.165440567574208, 0.171978821061628, 0.178699687278197, 0.185598818549075, 0.192664398770189, 0.199905517315959, 0.207295656637324, 0.214855100468329, 0.222547692489362, 0.230393493253638, 0.238360207280635, 0.246455151549793, 0.254657843700853, 0.262962117384979, 0.271355962870494, 0.279823407558889, 0.288356729520398, 0.29693478313137, 0.30554909571733, 0.314178927079256, 0.322809196632579, 0.33142374633836, 0.34000115135719, 0.34852678287039, 0.356978243850678, 0.365336286020657, 0.373584446265418, 0.381692112256306, 0.389656240070299, 0.397427685675839, 0.405020586381095, 0.412372188033242, 0.419501450640756, 0.42635294093303, 0.43293039677813, 0.439197951101347, 0.445136817114889, 0.450738597438507, 0.455954934148608, 0.460812443548202, 0.465226673340035, 0.469258274243541, 0.472804634723269, 0.475929761612576, 0.478555136029996, 0.480711608251192, 0.482361285409861, 0.483496787740908, 0.484126023022553, 0.484199659955106, 0.48377505004622, 0.482758800135345, 0.481250207182057, 0.479139552523101, 0.476525923190751, 0.473336185269251, 0.469626050930343, 0.465373518668837, 0.460591637350396, 0.455307903711616, 0.449495478202502, 0.443227443216616, 0.4364419016904, 0.429244272408768, 0.42156568162684, 0.413505471579226, 0.405030052939686, 0.396200583104986, 0.38702384493679, 0.377530297082519, 0.367757792078124, 0.357714983138924, 0.34746012491355, 0.336989954670091, 0.326369501824389, 0.315600243916584, 0.304735941413979, 0.293795073540449, 0.282814124987773, 0.271822226822539, 0.260848941073105, 0.249922524177412, 0.239075532470855, 0.228324608243385, 0.217714322337107, 0.207242832239666, 0.196966625478683, 0.186872830841579, 0.177010988967038, 0.167376631754878, 0.158000370170269];

    const d = density(eruptions, nrd0(boxplotStats(eruptions)), 200);
    expect(d.x.length).toBe(200);
    expect(d.y.length).toBe(200);
    for (let i = 0; i < d.x.length; i++) {
        expect(d.x[i]).toBeCloseTo(x[i]);
        expect(d.y[i]).toBeCloseTo(y[i]);
    }
    x.push(Number.NaN);
    y.push(Number.NaN);
    expect(d.x.length).toBe(200);
    expect(d.y.length).toBe(200);
    for (let i = 0; i < d.x.length; i++) {
        expect(d.x[i]).toBeCloseTo(x[i]);
        expect(d.y[i]).toBeCloseTo(y[i]);
    }
});
