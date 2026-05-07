// Merge dos blocos 1 + 2 da Gabriela. Retorna o mesmo formato do gabriela-data.js
// mas com dados de TODAS as aulas geradas até agora.

const block1 = require('./gabriela-data');
const block2 = require('./gabriela-data-block2');

const BLOCK_LESSONS = [1, 2, 3, 4, 5, 21, 22, 23, 24, 25];

function mergeMaps(...maps) {
  return Object.assign({}, ...maps);
}

const merged = {
  studentInfo: block1.studentInfo,
  lessonTitles: block1.lessonTitles,
  // Maps por aula — mescla blocos 1 e 2
  lessonPromises: mergeMaps(block1.lessonPromises, block2.lessonPromises),
  lessonImages: mergeMaps(block1.lessonImages, block2.lessonImages),
  lessonHeaderImages: mergeMaps(block1.lessonHeaderImages, block2.lessonHeaderImages),
  stampImages: mergeMaps(block1.stampImages, block2.stampImages),
  stampLabels: mergeMaps(block1.stampLabels, block2.stampLabels),
  vocab: mergeMaps(block1.vocab, block2.vocab),
  matching: mergeMaps(block1.matching, block2.matching),
  fillIn: mergeMaps(block1.fillIn, block2.fillIn),
  multipleChoice: mergeMaps(block1.multipleChoice, block2.multipleChoice),
  ordering: mergeMaps(block1.ordering, block2.ordering),
  pronunciation: mergeMaps(block1.pronunciation, block2.pronunciation),
  thinkAboutIt: mergeMaps(block1.thinkAboutIt, block2.thinkAboutIt),
  survivalCards: mergeMaps(block1.survivalCards, block2.survivalCards),
  grammarTips: mergeMaps(block1.grammarTips, block2.grammarTips),
  lessonObjectives: mergeMaps(block1.lessonObjectives, block2.lessonObjectives),
  homework: mergeMaps(block1.homework, block2.homework),
  ccqs: mergeMaps(block1.ccqs, block2.ccqs),
  obstacles: mergeMaps(block1.obstacles, block2.obstacles),
  dialogues: mergeMaps(block1.dialogues, block2.dialogues),
  oralDrills: mergeMaps(block1.oralDrills, block2.oralDrills),
  errorCorrection: mergeMaps(block1.errorCorrection, block2.errorCorrection),
  productionScenarios: mergeMaps(block1.productionScenarios, block2.productionScenarios),
  checklistItems: mergeMaps(block1.checklistItems, block2.checklistItems),
  BLOCK_LESSONS,
};

module.exports = merged;
