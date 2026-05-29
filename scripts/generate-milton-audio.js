const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'milton-sayegh');

// Two voices: Arthur for short phrases (1-2 words), Ellen for longer (3+ words)
const VOICE_ARTHUR = 'sfJopaWaOtauCD3HKX6Q'; // Arthur
const VOICE_ELLEN = 'BIvP0GN1cAtSRTxNHnWS';  // Ellen

// All unique phrase → filename mappings from milton-sayegh.html audioMap
// Deduplicated by filename (contractions and full forms share the same file)
const PHRASES = [
  { text: "export", file: "export.mp3" },
  { text: "luxury goods", file: "luxury_goods.mp3" },
  { text: "jewelry", file: "jewelry.mp3" },
  { text: "board meeting", file: "board_meeting.mp3" },
  { text: "negotiation", file: "negotiation.mp3" },
  { text: "deal", file: "deal.mp3" },
  { text: "headquarters", file: "headquarters.mp3" },
  { text: "overseas", file: "overseas.mp3" },
  { text: "misunderstanding", file: "misunderstanding.mp3" },
  { text: "fluency", file: "fluency.mp3" },
  { text: "luxury segment", file: "luxury_segment.mp3" },
  { text: "distributor", file: "distributor.mp3" },
  { text: "wholesale", file: "wholesale.mp3" },
  { text: "retail", file: "retail.mp3" },
  { text: "consignment", file: "consignment.mp3" },
  { text: "portfolio", file: "portfolio.mp3" },
  { text: "gem", file: "gem.mp3" },
  { text: "hallmark", file: "hallmark.mp3" },
  { text: "terms", file: "terms.mp3" },
  { text: "clause", file: "clause.mp3" },
  { text: "leverage", file: "leverage.mp3" },
  { text: "concession", file: "concession.mp3" },
  { text: "counterpart", file: "counterpart.mp3" },
  { text: "liability", file: "liability.mp3" },
  { text: "binding", file: "binding.mp3" },
  { text: "breach", file: "breach.mp3" },
  { text: "amendment", file: "amendment.mp3" },
  { text: "settlement", file: "settlement.mp3" },
  { text: "outcome", file: "outcome.mp3" },
  { text: "forecast", file: "forecast.mp3" },
  { text: "margin", file: "margin.mp3" },
  { text: "premium", file: "premium.mp3" },
  { text: "acquisition", file: "acquisition.mp3" },
  { text: "merger", file: "merger.mp3" },
  { text: "rival", file: "rival.mp3" },
  { text: "turnover", file: "turnover.mp3" },
  { text: "overhead", file: "overhead.mp3" },
  { text: "stakeholder", file: "stakeholder.mp3" },
  { text: "consequence", file: "consequence.mp3" },
  { text: "implication", file: "implication.mp3" },
  { text: "sustainable", file: "sustainable.mp3" },
  { text: "trajectory", file: "trajectory.mp3" },
  { text: "fragile", file: "fragile.mp3" },
  { text: "momentum", file: "momentum.mp3" },
  { text: "disruption", file: "disruption.mp3" },
  { text: "niche", file: "niche.mp3" },
  { text: "compliance", file: "compliance.mp3" },
  { text: "audit", file: "audit.mp3" },
  { text: "run a business", file: "run_a_business.mp3" },
  { text: "expand operations", file: "expand_operations.mp3" },
  { text: "manage a portfolio", file: "manage_a_portfolio.mp3" },
  { text: "close a deal", file: "close_a_deal.mp3" },
  { text: "reach an agreement", file: "reach_an_agreement.mp3" },
  { text: "make a concession", file: "make_a_concession.mp3" },
  { text: "set the terms", file: "set_the_terms.mp3" },
  { text: "breach a contract", file: "breach_a_contract.mp3" },
  { text: "come up with", file: "come_up_with.mp3" },
  { text: "look into", file: "look_into.mp3" },
  { text: "carry out", file: "carry_out.mp3" },
  { text: "maintain momentum", file: "maintain_momentum.mp3" },
  { text: "ensure compliance", file: "ensure_compliance.mp3" },
  { text: "disrupt the market", file: "disrupt_the_market.mp3" },
  { text: "identify a niche", file: "identify_a_niche.mp3" },
  { text: "phase out", file: "phase_out.mp3" },
  { text: "bring about", file: "bring_about.mp3" },
  { text: "set out", file: "set_out.mp3" },
  { text: "read between the lines", file: "read_between_the_lines.mp3" },
  { text: "a double-edged sword", file: "a_double_edged_sword.mp3" },
  { text: "the tip of the iceberg", file: "the_tip_of_the_iceberg.mp3" },
  { text: "My company exports luxury jewelry to the United States.", file: "my_company_exports_luxury_jewelry_to_the_united_states.mp3" },
  { text: "We specialize in luxury goods for the international market.", file: "we_specialize_in_luxury_goods_for_the_international_market.mp3" },
  { text: "The jewelry industry requires precision and trust.", file: "the_jewelry_industry_requires_precision_and_trust.mp3" },
  { text: "I attend the board meeting at my condo in Miami every month.", file: "i_attend_the_board_meeting_at_my_condo_in_miami_every_month.mp3" },
  { text: "A good negotiation requires clarity and confidence.", file: "a_good_negotiation_requires_clarity_and_confidence.mp3" },
  { text: "We closed a major deal with a new distributor last quarter.", file: "we_closed_a_major_deal_with_a_new_distributor_last_quarter.mp3" },
  { text: "Our headquarters is in Sao Paulo, but we operate in the U.S.", file: "our_headquarters_is_in_sao_paulo_but_we_operate_in_the_us.mp3" },
  { text: "I travel overseas at least four times a year.", file: "i_travel_overseas_at_least_four_times_a_year.mp3" },
  { text: "I want to avoid any misunderstanding in important meetings.", file: "i_want_to_avoid_any_misunderstanding_in_important_meetings.mp3" },
  { text: "My goal is to recover my fluency in English.", file: "my_goal_is_to_recover_my_fluency_in_english.mp3" },
  { text: "I'm responsible for all export operations.", file: "im_responsible_for_all_export_operations.mp3" },
  { text: "I deal with international clients on a daily basis.", file: "i_deal_with_international_clients_on_a_daily_basis.mp3" },
  { text: "My company operates in the luxury jewelry segment.", file: "my_company_operates_in_the_luxury_jewelry_segment.mp3" },
  { text: "I'm sorry, I didn't quite catch that.", file: "im_sorry_i_didnt_quite_catch_that.mp3" },
  { text: "Could you say that again, please?", file: "could_you_say_that_again_please.mp3" },
  { text: "Let me think about that for a moment.", file: "let_me_think_about_that_for_a_moment.mp3" },
  { text: "What I mean is...", file: "what_i_mean_is.mp3" },
  { text: "My name is Milton Sayegh. I'm in the jewelry business.", file: "my_name_is_milton_sayegh_im_in_the_jewelry_business.mp3" },
  { text: "I'm responsible for the export operations of my company.", file: "im_responsible_for_the_export_operations_of_my_company.mp3" },
  { text: "My goal is to recover my fluency in business English.", file: "my_goal_is_to_recover_my_fluency_in_business_english.mp3" },
  { text: "Hi there. I'm James Whitfield from Whitfield Gems in New York. Are you in the jewelry business?", file: "hi_there_im_james_whitfield_from_whitfield_gems.mp3" },
  { text: "Yes, I am. My name is Milton Sayegh. I run an export company based in Sao Paulo.", file: "yes_i_am_my_name_is_milton_sayegh_i_run_an_export_company.mp3" },
  { text: "Oh, interesting. What kind of jewelry do you export?", file: "oh_interesting_what_kind_of_jewelry_do_you_export.mp3" },
  { text: "We specialize in luxury goods — precious stones, gold pieces, and custom designs.", file: "we_specialize_in_luxury_goods_precious_stones_gold_pieces.mp3" },
  { text: "That's impressive. Do you have an office in the U.S.?", file: "thats_impressive_do_you_have_an_office_in_the_us.mp3" },
  { text: "We do. Our American headquarters is in Miami. I travel overseas several times a year.", file: "we_do_our_american_headquarters_is_in_miami.mp3" },
  { text: "I see. How long have you been in the export business?", file: "i_see_how_long_have_you_been_in_the_export_business.mp3" },
  { text: "For over thirty years. But I'm working on improving my English for negotiations.", file: "for_over_thirty_years_but_im_working_on_improving_my_english.mp3" },
  { text: "Your English sounds good to me. Do you deal with many American distributors?", file: "your_english_sounds_good_to_me_do_you_deal_with_many.mp3" },
  { text: "A few, but I want to expand. I believe clear communication is key to avoiding misunderstandings.", file: "a_few_but_i_want_to_expand_i_believe_clear_communication.mp3" },
  { text: "Absolutely. Let's schedule a meeting to discuss a possible deal.", file: "absolutely_lets_schedule_a_meeting_to_discuss_a_possible_deal.mp3" },
  { text: "That would be great. I'm responsible for all business decisions, so we can move quickly.", file: "that_would_be_great_im_responsible_for_all_business_decisions.mp3" },
  { text: "Good morning. My name is Milton Sayegh.", file: "good_morning_my_name_is_milton_sayegh.mp3" },
  { text: "I'm from Sao Paulo, Brazil.", file: "im_from_sao_paulo_brazil.mp3" },
  { text: "I run a luxury jewelry export company.", file: "i_run_a_luxury_jewelry_export_company.mp3" },
  { text: "We operate in the United States and Brazil.", file: "we_operate_in_the_united_states_and_brazil.mp3" },
  { text: "It's a pleasure to meet you.", file: "its_a_pleasure_to_meet_you.mp3" },
  { text: "Our company operates in the luxury segment of the jewelry market.", file: "our_company_operates_in_the_luxury_segment_of_the_jewelry_market.mp3" },
  { text: "We work with three distributors in the United States.", file: "we_work_with_three_distributors_in_the_united_states.mp3" },
  { text: "We sell wholesale to retailers across the country.", file: "we_sell_wholesale_to_retailers_across_the_country.mp3" },
  { text: "Some of our pieces are available in retail stores.", file: "some_of_our_pieces_are_available_in_retail_stores.mp3" },
  { text: "We offer consignment terms to selected partners.", file: "we_offer_consignment_terms_to_selected_partners.mp3" },
  { text: "Our portfolio includes over two hundred unique designs.", file: "our_portfolio_includes_over_two_hundred_unique_designs.mp3" },
  { text: "Brazilian gems are known for their exceptional quality.", file: "brazilian_gems_are_known_for_their_exceptional_quality.mp3" },
  { text: "Quality is the hallmark of our brand.", file: "quality_is_the_hallmark_of_our_brand.mp3" },
  { text: "We specialize in luxury jewelry for the international market.", file: "we_specialize_in_luxury_jewelry_for_the_international_market.mp3" },
  { text: "We specialize in...", file: "we_specialize_in.mp3" },
  { text: "Our company currently exports to...", file: "our_company_currently_exports_to.mp3" },
  { text: "Our company was founded over thirty years ago.", file: "our_company_was_founded_over_thirty_years_ago.mp3" },
  { text: "We specialize in luxury jewelry for the export market.", file: "we_specialize_in_luxury_jewelry_for_the_export_market.mp3" },
  { text: "We work with distributors in the United States.", file: "we_work_with_distributors_in_the_united_states.mp3" },
  { text: "Quality and precision are the hallmarks of our brand.", file: "quality_and_precision_are_the_hallmarks_of_our_brand.mp3" },
  { text: "Our company has been in business for over thirty years.", file: "our_company_has_been_in_business_for_over_thirty_years.mp3" },
  { text: "I'd like to discuss a possible partnership.", file: "id_like_to_discuss_a_possible_partnership.mp3" },
  { text: "Could you tell me more about your company?", file: "could_you_tell_me_more_about_your_company.mp3" },
  { text: "We currently export to the United States.", file: "we_currently_export_to_the_united_states.mp3" },
  { text: "The terms of the agreement were not favorable.", file: "the_terms_of_the_agreement_were_not_favorable.mp3" },
  { text: "There was a problematic clause in the contract.", file: "there_was_a_problematic_clause_in_the_contract.mp3" },
  { text: "Having exclusive products gives us leverage in negotiations.", file: "having_exclusive_products_gives_us_leverage_in_negotiations.mp3" },
  { text: "Making a concession can strengthen a business relationship.", file: "making_a_concession_can_strengthen_a_business_relationship.mp3" },
  { text: "My American counterpart suggested different payment terms.", file: "my_american_counterpart_suggested_different_payment_terms.mp3" },
  { text: "The contract defines each party's liability.", file: "the_contract_defines_each_partys_liability.mp3" },
  { text: "A binding agreement cannot be easily changed.", file: "a_binding_agreement_cannot_be_easily_changed.mp3" },
  { text: "A breach of contract can result in legal action.", file: "a_breach_of_contract_can_result_in_legal_action.mp3" },
  { text: "We proposed an amendment to the original terms.", file: "we_proposed_an_amendment_to_the_original_terms.mp3" },
  { text: "Both parties reached a settlement after months of negotiation.", file: "both_parties_reached_a_settlement_after_months_of_negotiation.mp3" },
  { text: "We should have reviewed the terms before signing the contract.", file: "we_should_have_reviewed_the_terms_before_signing.mp3" },
  { text: "If I had known about the clause, I would have negotiated differently.", file: "if_i_had_known_about_the_clause_i_would_have_negotiated.mp3" },
  { text: "We should have discussed this earlier.", file: "we_should_have_discussed_this_earlier.mp3" },
  { text: "I must have missed that detail.", file: "i_must_have_missed_that_detail.mp3" },
  { text: "Could you walk me through the terms?", file: "could_you_walk_me_through_the_terms.mp3" },
  { text: "Let me look into that clause.", file: "let_me_look_into_that_clause.mp3" },
  { text: "I believe we can reach an agreement.", file: "i_believe_we_can_reach_an_agreement.mp3" },
  { text: "The outcome of the merger was positive for both companies.", file: "the_outcome_of_the_merger_was_positive.mp3" },
  { text: "The market forecast suggests growth in luxury exports.", file: "the_market_forecast_suggests_growth_in_luxury_exports.mp3" },
  { text: "Our profit margin increased by five percent this year.", file: "our_profit_margin_increased_by_five_percent.mp3" },
  { text: "We position our jewelry as a premium product.", file: "we_position_our_jewelry_as_a_premium_product.mp3" },
  { text: "The acquisition of a smaller brand expanded our portfolio.", file: "the_acquisition_of_a_smaller_brand_expanded_our_portfolio.mp3" },
  { text: "A merger with a local company would give us market access.", file: "a_merger_with_a_local_company_would_give_us_market_access.mp3" },
  { text: "Our main rival recently entered the American market.", file: "our_main_rival_recently_entered_the_american_market.mp3" },
  { text: "Annual turnover exceeded ten million dollars last year.", file: "annual_turnover_exceeded_ten_million_dollars.mp3" },
  { text: "Keeping overhead low is essential for export businesses.", file: "keeping_overhead_low_is_essential.mp3" },
  { text: "All stakeholders must approve the new strategy.", file: "all_stakeholders_must_approve_the_new_strategy.mp3" },
  { text: "If we had invested earlier, we would have captured the market.", file: "if_we_had_invested_earlier_we_would_have_captured.mp3" },
  { text: "If we had expanded to the American market earlier, we would have doubled our revenue.", file: "if_we_had_expanded_to_the_american_market_earlier.mp3" },
  { text: "The acquisition would have been a double-edged sword for our company.", file: "the_acquisition_would_have_been_a_double_edged_sword.mp3" },
  { text: "If we had known earlier, we would have acted differently.", file: "if_we_had_known_earlier_we_would_have_acted_differently.mp3" },
  { text: "The outcome was not what we expected.", file: "the_outcome_was_not_what_we_expected.mp3" },
  { text: "Looking back, we should have been more cautious.", file: "looking_back_we_should_have_been_more_cautious.mp3" },
  { text: "That decision was a double-edged sword.", file: "that_decision_was_a_double_edged_sword.mp3" },
  { text: "What would you have done in my position?", file: "what_would_you_have_done_in_my_position.mp3" },
  { text: "Every business decision has long-term consequences.", file: "every_business_decision_has_long_term_consequences.mp3" },
  { text: "The implication of this change is significant.", file: "the_implication_of_this_change_is_significant.mp3" },
  { text: "A sustainable business model is essential for growth.", file: "a_sustainable_business_model_is_essential_for_growth.mp3" },
  { text: "The company's trajectory has been consistently upward.", file: "the_companys_trajectory_has_been_consistently_upward.mp3" },
  { text: "International partnerships can be fragile without clear communication.", file: "international_partnerships_can_be_fragile.mp3" },
  { text: "We need to maintain momentum in our expansion.", file: "we_need_to_maintain_momentum_in_our_expansion.mp3" },
  { text: "Market disruption creates both risks and opportunities.", file: "market_disruption_creates_both_risks_and_opportunities.mp3" },
  { text: "We found our niche in luxury Brazilian gemstones.", file: "we_found_our_niche_in_luxury_brazilian_gemstones.mp3" },
  { text: "Compliance with U.S. regulations is mandatory.", file: "compliance_with_us_regulations_is_mandatory.mp3" },
  { text: "The annual audit revealed no issues with our operations.", file: "the_annual_audit_revealed_no_issues.mp3" },
  { text: "If we had invested in digital in 2015, we would be leading the market now.", file: "if_we_had_invested_in_digital_in_2015.mp3" },
  { text: "If we had not built strong partnerships, we would not be where we are today.", file: "if_we_had_not_built_strong_partnerships.mp3" },
  { text: "The compliance issues were just the tip of the iceberg.", file: "the_compliance_issues_were_just_the_tip_of_the_iceberg.mp3" },
  { text: "If we had not expanded overseas, we would not be this successful today.", file: "if_we_had_not_expanded_overseas.mp3" },
  { text: "That was just the tip of the iceberg.", file: "that_was_just_the_tip_of_the_iceberg.mp3" },
  { text: "We need to ensure compliance with all regulations.", file: "we_need_to_ensure_compliance_with_all_regulations.mp3" },
  { text: "The trajectory of our business has been very positive.", file: "the_trajectory_of_our_business_has_been_very_positive.mp3" },
  { text: "We must maintain momentum in our expansion.", file: "we_must_maintain_momentum_in_our_expansion.mp3" },
  { text: "If we had not invested in compliance ten years ago we would not be operating in the United States today.", file: "if_we_had_not_invested_in_compliance_ten_years_ago.mp3" },
  { text: "Brazil exports many precious stones to international markets.", file: "brazil_exports_many_precious_stones.mp3" },
  { text: "Luxury goods require careful packaging for shipping.", file: "luxury_goods_require_careful_packaging.mp3" },
  { text: "The jewelry sector in Brazil is worth billions.", file: "the_jewelry_sector_in_brazil_is_worth_billions.mp3" },
  { text: "The next board meeting is scheduled for June.", file: "the_next_board_meeting_is_scheduled_for_june.mp3" },
  { text: "Every successful negotiation starts with good preparation.", file: "every_successful_negotiation_starts_with_good_preparation.mp3" },
  { text: "The deal includes exclusive distribution rights.", file: "the_deal_includes_exclusive_distribution_rights.mp3" },
  { text: "Many international companies have their headquarters in New York.", file: "many_international_companies_have_their_headquarters.mp3" },
  { text: "Working overseas can be challenging but rewarding.", file: "working_overseas_can_be_challenging_but_rewarding.mp3" },
  { text: "Clear communication prevents misunderstanding in business.", file: "clear_communication_prevents_misunderstanding.mp3" },
  { text: "Fluency comes with consistent practice and exposure.", file: "fluency_comes_with_consistent_practice_and_exposure.mp3" },
  { text: "The luxury segment demands exceptional craftsmanship.", file: "the_luxury_segment_demands_exceptional_craftsmanship.mp3" },
  { text: "A reliable distributor is essential for market expansion.", file: "a_reliable_distributor_is_essential.mp3" },
  { text: "Wholesale pricing requires minimum order quantities.", file: "wholesale_pricing_requires_minimum_order_quantities.mp3" },
  { text: "Retail customers expect premium packaging.", file: "retail_customers_expect_premium_packaging.mp3" },
  { text: "Consignment reduces risk for new partners.", file: "consignment_reduces_risk_for_new_partners.mp3" },
  { text: "Updating your portfolio keeps the brand fresh.", file: "updating_your_portfolio_keeps_the_brand_fresh.mp3" },
  { text: "Each gem in our collection is certified.", file: "each_gem_in_our_collection_is_certified.mp3" },
  { text: "Innovation has become the hallmark of successful companies.", file: "innovation_has_become_the_hallmark.mp3" },
  { text: "Milton, tell me about your company. What makes it unique?", file: "milton_tell_me_about_your_company.mp3" },
  { text: "Well, we've been in the luxury segment for over thirty years. We specialize in exporting fine jewelry.", file: "well_weve_been_in_the_luxury_segment.mp3" },
  { text: "Who are your main clients?", file: "who_are_your_main_clients.mp3" },
  { text: "We work with distributors in the United States. Some buy wholesale, others prefer consignment.", file: "we_work_with_distributors_some_buy_wholesale.mp3" },
  { text: "That's flexible. How many designs do you offer?", file: "thats_flexible_how_many_designs_do_you_offer.mp3" },
  { text: "Our portfolio currently includes over two hundred unique pieces. Each gem is carefully selected.", file: "our_portfolio_currently_includes_over_two_hundred.mp3" },
  { text: "What would you say is the hallmark of your brand?", file: "what_would_you_say_is_the_hallmark.mp3" },
  { text: "Quality and trust. Our clients know that every piece meets the highest standards.", file: "quality_and_trust_our_clients_know.mp3" },
  { text: "Are you looking to expand?", file: "are_you_looking_to_expand.mp3" },
  { text: "Yes, we're currently expanding our operations to reach more retail markets in the U.S.", file: "yes_were_currently_expanding_our_operations.mp3" },
  { text: "The market is definitely growing. What's your competitive advantage?", file: "the_market_is_definitely_growing.mp3" },
  { text: "Our thirty years of experience, combined with direct access to Brazilian gems. That's hard to replicate.", file: "our_thirty_years_of_experience_combined.mp3" },
  { text: "My company exports luxury jewelry.", file: "my_company_exports_luxury_jewelry.mp3" },
  { text: "I'm working on improving my English.", file: "im_working_on_improving_my_english.mp3" },
  { text: "Our headquarters is in Sao Paulo.", file: "our_headquarters_is_in_sao_paulo.mp3" },
  { text: "I travel overseas four times a year.", file: "i_travel_overseas_four_times_a_year.mp3" },
  { text: "I'm responsible for all operations.", file: "im_responsible_for_all_operations.mp3" },
  { text: "We specialize in luxury goods.", file: "we_specialize_in_luxury_goods.mp3" },
  { text: "The negotiation requires clarity.", file: "the_negotiation_requires_clarity.mp3" },
  { text: "We closed a major deal last quarter.", file: "we_closed_a_major_deal_last_quarter.mp3" },
  { text: "It would appear that...", file: "it_would_appear_that.mp3" },
  { text: "One could argue that...", file: "one_could_argue_that.mp3" },
];

// Determine voice: 1-2 words = Arthur, 3+ words = alternate Arthur/Ellen
let ellenToggle = false;
function getVoiceForPhrase(text) {
  const clean = text.replace(/[^a-zA-Z0-9' -]/g, '').trim();
  const wordCount = clean.split(/\s+/).filter(w => w).length;
  if (wordCount <= 2) {
    return { id: VOICE_ARTHUR, name: 'Arthur' };
  }
  // 3+ words: alternate between Arthur and Ellen
  ellenToggle = !ellenToggle;
  return ellenToggle
    ? { id: VOICE_ELLEN, name: 'Ellen' }
    : { id: VOICE_ARTHUR, name: 'Arthur' };
}

async function generateOne(text, voiceId, retries = 2) {
  const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;
  const body = JSON.stringify({
    text,
    model_id: 'eleven_monolingual_v1',
    voice_settings: { stability: 0.5, similarity_boost: 0.75 }
  });

  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'xi-api-key': API_KEY,
          'Accept': 'audio/mpeg'
        },
        body
      });

      if (res.status === 429) {
        console.log(`  Rate limited, waiting 30s...`);
        await new Promise(r => setTimeout(r, 30000));
        continue;
      }

      if (!res.ok) {
        const err = await res.text();
        throw new Error(`HTTP ${res.status}: ${err}`);
      }

      const buffer = Buffer.from(await res.arrayBuffer());
      return buffer;
    } catch (e) {
      if (attempt === retries) throw e;
      await new Promise(r => setTimeout(r, 5000));
    }
  }
}

async function main() {
  if (!API_KEY) { console.error('No ELEVENLABS_API_KEY set in environment.'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  // Deduplicate by filename (some phrases share the same file)
  const seen = new Set();
  const uniquePhrases = [];
  for (const p of PHRASES) {
    if (!seen.has(p.file)) {
      seen.add(p.file);
      uniquePhrases.push(p);
    }
  }

  const total = uniquePhrases.length;
  let generated = 0, skipped = 0, failed = 0;

  console.log(`Milton Sayegh Audio Generator`);
  console.log(`Total unique files to generate: ${total}`);
  console.log(`Output: ${OUTPUT_DIR}`);
  console.log(`Voices: Arthur (1-2 words) + Ellen (3+ words, alternating)`);
  console.log('---');

  for (let i = 0; i < uniquePhrases.length; i++) {
    const { text, file: filename } = uniquePhrases[i];
    const filepath = path.join(OUTPUT_DIR, filename);

    // Skip if already exists
    if (fs.existsSync(filepath)) {
      skipped++;
      continue;
    }

    const voice = getVoiceForPhrase(text);

    try {
      process.stdout.write(`[${i+1}/${total}] (${voice.name}) "${text.substring(0, 50)}${text.length > 50 ? '...' : ''}" `);
      const buffer = await generateOne(text, voice.id);
      fs.writeFileSync(filepath, buffer);
      generated++;
      console.log('OK');
      // Rate limit: 120ms between requests
      await new Promise(r => setTimeout(r, 120));
    } catch (e) {
      console.log(`FAILED: ${e.message}`);
      failed++;
    }
  }

  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Failed: ${failed}`);
  console.log(`Total unique files: ${total}`);
}

main();
